import argparse
import sys
from pathlib import Path
from .logger import Logger
from .license_manager import LicenseManager
from .scanner.basic import BasicScanner
from .scanner.advanced import AdvancedScanner
from .constants import TOOL_NAME, VERSION, RECIPIENT_WALLET, MIN_SOL_THRESHOLD

def main():
    parser = argparse.ArgumentParser(
        description=f"{TOOL_NAME} - Educational Security Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--unlock", action="store_true", help="Unlock premium features via Solana donation")
    parser.add_argument("--verbose", action="store_true", help="Show detailed scanning progress")
    parser.add_argument("--generate-gitignore", action="store_true", help="Generate a recommended .gitignore (Premium)")
    parser.add_argument("--install-hook", action="store_true", help="Install a pre-commit hook (Premium)")
    
    args = parser.parse_args()
    
    Logger.bold(f"Welcome to {TOOL_NAME} v{VERSION} 🛡️")
    print("Helping you keep your secrets safe and your repos clean.\n")

    license_mgr = LicenseManager()

    if args.unlock:
        handle_unlock(license_mgr)
        return

    # Check for premium status
    is_premium = license_mgr.is_premium
    
    if is_premium:
        Logger.success("Premium Mode Active 💎")
        scanner = AdvancedScanner(Path.cwd(), verbose=args.verbose)
    else:
        Logger.info("Free Version - Basic scanning only.")
        scanner = BasicScanner(Path.cwd())

    # Run the scan
    scanner.scan()
    scanner.report()

    # Premium only features
    if args.generate_gitignore:
        if is_premium:
            scanner.generate_gitignore()
        else:
            Logger.premium_locked("Auto .gitignore Generator")

    if args.install_hook:
        if is_premium:
            scanner.generate_pre_commit_hook()
        else:
            Logger.premium_locked("Pre-commit Hook Installation")

    if not is_premium:
        print("\n---")
        Logger.info("Want more? Premium includes AWS/Stripe detection, .gitignore generation, and more!")
        print(f"Run 'safe-push --unlock' to upgrade.")

def handle_unlock(license_mgr: LicenseManager):
    Logger.header("Unlock Premium Features")
    print(f"To unlock premium features, please send at least {MIN_SOL_THRESHOLD} SOL to:")
    Logger.bold(RECIPIENT_WALLET)
    print("\nThis supports the project and teaches you about decentralized verification!")
    
    print("\nAfter sending, enter your details below:")
    sender = input("Your Solana Wallet Address: ").strip()
    txid = input("Transaction Hash (TXID): ").strip()
    
    if not sender or not txid:
        Logger.error("Wallet address and TXID are required.")
        return

    if license_mgr.verify_and_unlock(sender, txid):
        Logger.success("Everything set! You can now use all premium features.")
    else:
        Logger.error("Verification failed. Please check your transaction and try again.")

if __name__ == "__main__":
    main()
