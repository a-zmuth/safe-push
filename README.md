# safe-push 🛡️

An educational, beginner-friendly Python CLI tool that teaches you about accidental sensitive data exposure while helping you keep your repositories clean.

## 🌟 Why safe-push?

Accidentally pushing a `.env` file or a hardcoded API key to GitHub is a rite of passage for many developers—but it's also a major security risk! `safe-push` helps you identify these risks *before* you push, explaining **why** certain files shouldn't be shared.

Perfect for "vibe coders" and beginners who want to stay safe while learning.

## 🚀 Features

### 🆓 Free Tier (Always)
- **Scan Current Directory**: Detects common mistakes like `.env` files, `__pycache__`, and `venv` folders.
- **Basic Secret Detection**: Finds generic API keys and tokens.
- **Educational Insights**: Explains the danger of each finding so you learn as you go.
- **No Data Leaves Your Machine**: Your code stays local. Always.

### 💎 Premium Features
- **Advanced Secret Scanning**: Deep detection for AWS, Stripe, OpenAI, Firebase, and more.
- **Auto .gitignore Generator**: Quickly create a recommended `.gitignore` for your Python projects.
- **Pre-commit Hook Template**: Automatically scan your code every time you try to `git commit`.
- **Verbose Mode**: See exactly what's happening under the hood.

## 🛠️ Installation

```bash
pip install safe-push
```

## 📖 How to Use

Simply run the tool in your project's root directory:

```bash
safe-push
```

### Options
- `safe-push --verbose`: Show a detailed breakdown of the scan.
- `safe-push --unlock`: Learn how to unlock premium features.
- `safe-push --generate-gitignore`: (Premium) Create a recommended `.gitignore`.
- `safe-push --install-hook`: (Premium) Install a Git pre-commit hook.

## 🔓 Unlocking Premium (The Solana Way)

We use a simple, decentralized verification system. No accounts, no credit cards.

1. Donate at least **0.005 SOL** (~$2) to the recipient wallet shown when you run `safe-push --unlock`.
2. Enter your wallet address and the Transaction ID (TXID).
3. The CLI verifies the transaction directly on the Solana blockchain and unlocks your features locally!

## 🔒 Security & Privacy
- **Local Only**: This tool scans only your local directory.
- **Privacy First**: No data, code, or telemetry is ever sent to any server.
- **Transparency**: The only network call made is to a public Solana RPC endpoint for donation verification.

## 📜 License
MIT License. Feel free to use, learn, and share!

---
*Stay safe and keep coding!* 🚀
