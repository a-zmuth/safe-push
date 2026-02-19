import sys
from colorama import init, Style

# Initialise colorama for cross-platform terminal formatting (it was looking ugly on terminal without it.)
init(autoreset=True)

class Logger:
    """A simple, friendly logger for educational purposes."""

    @staticmethod
    def info(msg: str):
        print(f"ℹ️  {msg}")

    @staticmethod
    def success(msg: str):
        print(f"✅ {msg}")

    @staticmethod
    def warning(msg: str):
        print(f"⚠️  {msg}")

    @staticmethod
    def error(msg: str):
        print(f"❌ {msg}", file=sys.stderr)

    @staticmethod
    def header(msg: str):
        print(f"\n--- {msg} ---")

    @staticmethod
    def bold(msg: str):
        # Bold text using colorama
        print(f"{Style.BRIGHT}{msg}")

    @staticmethod
    def educate(title: str, body: str):
        print(f"\n🎓 {Style.BRIGHT}Why {title}?{Style.RESET_ALL}")
        print(f"   {body}")

    @staticmethod
    def premium_locked(feature: str):
        print(f"\n💎 {Style.BRIGHT}Premium Feature: {feature}{Style.RESET_ALL}")
        print(
            "   This is locked. Run 'safe-push --unlock' to learn how to access it via a small Solana donation!"
        )
