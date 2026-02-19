from pathlib import Path

TOOL_NAME = "safe-push 🛡️"
VERSION = "0.1.4"

RECIPIENT_WALLET = "GgANeKwJecCMPhna9HvZCtELUCg3c6snJZsqi8vx2JqW" 
MIN_SOL_THRESHOLD = 0.005  # Approximately $2 at current rates
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Local Storage
HOME_DIR = Path.home()
LICENSE_DIR = HOME_DIR / ".safe_push"
LICENSE_FILE = LICENSE_DIR / "license.json"

# Educational Links
GITIGNORE_DOCS = "https://git-scm.com/docs/gitignore"
VENV_DOCS = "https://docs.python.org/3/library/venv.html"
