import json
import requests
from pathlib import Path
import time
from .constants import RECIPIENT_WALLET, MIN_SOL_THRESHOLD, SOLANA_RPC_URL, LICENSE_FILE, LICENSE_DIR
from .logger import Logger

class LicenseManager:
    def __init__(self):
        self.is_premium = self._check_local_license()

    def _check_local_license(self) -> bool:
        """Checks if a valid license file exists locally."""
        if not LICENSE_FILE.exists():
            return False
        
        try:
            with open(LICENSE_FILE, "r") as f:
                data = json.load(f)
                # In a real app, we'd verify a signature or check the hash again.
                # For this educational tool, we check if the basic structure is there.
                return data.get("status") == "unlocked" and "txid" in data
        except (json.JSONDecodeError, IOError):
            return False

    def verify_and_unlock(self, sender_wallet: str, txid: str) -> bool:
        """
        Verifies a Solana transaction via public RPC.
        Returns True if valid and unlocks premium features.
        """
        Logger.info("Verifying transaction on the Solana blockchain...")
        
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTransaction",
            "params": [
                txid,
                {"encoding": "json", "maxSupportedTransactionVersion": 0}
            ]
        }

        try:
            response = requests.post(SOLANA_RPC_URL, json=payload, timeout=15)
            response.raise_for_status()
            result = response.json().get("result")

            if not result:
                Logger.error("Transaction not found. Ensure the TXID is correct and confirmed.")
                return False

            # Extract transaction details
            # Note: Solana API structure can be kinda complex.
            meta = result.get("meta", {})
            transaction = result.get("transaction", {})
            message = transaction.get("message", {})
            account_keys = message.get("accountKeys", [])

            # 1. Check if confirmed
            if meta.get("err"):
                Logger.error("Transaction failed on-chain.")
                return False

            # 2. Check recipient and amount
            # This is a simplified check for a direct SOL transfer
            post_balances = meta.get("postBalances", [])
            pre_balances = meta.get("preBalances", [])
            
            recipient_index = -1
            for i, key in enumerate(account_keys):
                if key == RECIPIENT_WALLET:
                    recipient_index = i
                    break
            
            if recipient_index == -1:
                Logger.error(f"Recipient wallet {RECIPIENT_WALLET} not found in transaction.")
                return False

            # lamports to SOL (1 SOL = 10^9 lamports)
            amount_lamports = post_balances[recipient_index] - pre_balances[recipient_index]
            amount_sol = amount_lamports / 1_000_000_000

            if amount_sol < MIN_SOL_THRESHOLD:
                Logger.error(f"Amount {amount_sol} SOL is less than required {MIN_SOL_THRESHOLD} SOL.")
                return False

            # 3. Check sender
            sender_found = False
            for key in account_keys:
                if key == sender_wallet:
                    sender_found = True
                    break
            
            if not sender_found:
                Logger.error(f"Sender wallet {sender_wallet} not found in transaction.")
                return False

            # Success!
            self._save_license(sender_wallet, txid)
            self.is_premium = True
            Logger.success("Premium features unlocked! Thank you for your support. 🚀")
            return True

        except requests.exceptions.RequestException as e:
            Logger.error(f"Network error during verification: {e}")
            return False
        except Exception as e:
            Logger.error(f"An unexpected error occurred: {e}")
            return False

    def _save_license(self, wallet: str, txid: str):
        """Saves the license info locally."""
        LICENSE_DIR.mkdir(parents=True, exist_ok=True)
        license_data = {
            "status": "unlocked",
            "wallet": wallet,
            "txid": txid,
            "timestamp": time.time()
        }
        with open(LICENSE_FILE, "w") as f:
            json.dump(license_data, f, indent=4)
