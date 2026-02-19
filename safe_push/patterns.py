import re

# Basic patterns for free scanning
# These are beginner-level checks for common mistakes.

BASIC_DIR_PATTERNS = [
    "__pycache__",
    ".venv",
    "venv",
    "env",
    ".env",
    ".git",  # We don't necessarily want to scan inside .git
]

BASIC_FILE_PATTERNS = [
    ".env",
    ".env.local",
    ".env.dev",
    "secrets.py",
    "config.py",  # Sometimes contains secrets, worth a check
]

# Simple regex patterns for sensitive data
BASIC_SECRET_PATTERNS = {
    "Generic API Key": r"""(?i)(api[_-]?key|token|auth|password|secret)[\s]*[:=][\s]*['"]?([a-zA-Z0-9_\-]{16,})['"]?""",
}

EDUCATIONAL_CONTEXT = {
    ".env": "Contains environment variables, often including secrets like database passwords or API keys.",
    "__pycache__": "Python bytecode cache files. While not 'secret', they clutter repositories and are OS-dependent.",
    "venv": "Virtual environment folder. These contain installed packages and should be recreated by users, not pushed to Git.",
    ".venv": "Virtual environment folder. These contain installed packages and should be recreated by users, not pushed to Git.",
}
