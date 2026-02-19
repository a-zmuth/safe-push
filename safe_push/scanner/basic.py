import re
from pathlib import Path
from ..patterns import BASIC_DIR_PATTERNS, BASIC_FILE_PATTERNS, BASIC_SECRET_PATTERNS, EDUCATIONAL_CONTEXT
from ..logger import Logger

class BasicScanner:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.findings = []

    def scan(self):
        """Scans only the current working directory."""
        Logger.info(f"Scanning directory: {self.root_dir}")
        
        # 1. Check for dangerous directories/files by name
        for path in self.root_dir.iterdir():
            if path.is_dir() and path.name in BASIC_DIR_PATTERNS:
                self.findings.append({
                    "type": "directory",
                    "path": path.name,
                    "reason": EDUCATIONAL_CONTEXT.get(path.name, "Dangerous directory found.")
                })
            elif path.is_file() and path.name in BASIC_FILE_PATTERNS:
                self.findings.append({
                    "type": "file",
                    "path": path.name,
                    "reason": EDUCATIONAL_CONTEXT.get(path.name, "Dangerous file found.")
                })

        # 2. Check for basic secrets in common files
        # We only scan text-based files to avoid binary issues
        for path in self.root_dir.iterdir():
            if path.is_file() and self._is_text_file(path):
                self._scan_file_contents(path, BASIC_SECRET_PATTERNS)

    def _is_text_file(self, path: Path) -> bool:
        """Simple check to avoid scanning large binary files."""
        try:
            # Check file extension or try reading a small chunk
            if path.suffix.lower() in [".png", ".jpg", ".exe", ".pyc", ".zip"]:
                return False
            if path.stat().st_size > 1_000_000:  # 1MB limit for safety
                return False
            return True
        except Exception:
            return False

    def _scan_file_contents(self, path: Path, patterns: dict):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for name, regex in patterns.items():
                    if re.search(regex, content):
                        self.findings.append({
                            "type": "secret",
                            "path": path.name,
                            "pattern_name": name,
                            "reason": f"Potential {name} detected inside the file."
                        })
        except Exception as e:
            Logger.error(f"Could not read {path.name}: {e}")

    def report(self):
        if not self.findings:
            Logger.success("No common security risks found in the current directory!")
            return

        Logger.warning(f"Found {len(self.findings)} items to review:")
        for item in self.findings:
            if item["type"] == "directory":
                Logger.bold(f"📁 {item['path']}")
            elif item["type"] == "file":
                Logger.bold(f"📄 {item['path']}")
            else:
                Logger.bold(f"🔑 {item['path']} ({item['pattern_name']})")
            
            print(f"   {item['reason']}")
            
            # Educational moment
            key = item.get("path") if item["type"] != "secret" else ".env"  # Generic env advice for secrets
            if key in EDUCATIONAL_CONTEXT:
                Logger.educate(key, EDUCATIONAL_CONTEXT[key])
        
        # ✅ Fixed multi-line print
        print("\n💡 Tip: Add these to a .gitignore file to prevent them from being pushed to GitHub.")
