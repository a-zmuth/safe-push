import re

# Advanced patterns for premium users
# These target specific service keys. May add more stuff later.

PREMIUM_SECRET_PATTERNS = {
    "AWS Access Key ID": r"(?i)AKIA[0-9A-Z]{16}",

    "AWS Secret Access Key": r"""(?i)aws[_-]?secret[_-]?access[_-]?key[\s]*[:=][\s]*['"]?([a-zA-Z0-9/+=]{40})['"]?""",

    "Firebase Config": r"""(?i)apiKey[\s]*[:=][\s]*['"]?AIza[a-zA-Z0-9_-]{35}['"]?""",

    "JWT Secret": r"""(?i)(jwt|json[_-]?web[_-]?token)[_-]?(secret|key)[\s]*[:=][\s]*['"]?([a-zA-Z0-9_\-=]{32,})['"]?""",

    "Private Key": r"-----BEGIN[A-Z ]*PRIVATE KEY-----",

    "Stripe Secret Key": r"sk_live_[0-9a-zA-Z]{24}",

    "OpenAI API Key": r"sk-[a-zA-Z0-9]{32,}",
}


PREMIUM_EDUCATIONAL_CONTEXT = {
    "AWS": "AWS keys allow full control over your cloud infrastructure. If leaked, attackers can rack up thousands in charges.",
    "Firebase": "Firebase API keys are used for client-side auth but should still be restricted to prevent abuse.",
    "Stripe": "Live Stripe keys allow anyone to process payments or view customer data on your account.",
    "OpenAI": "OpenAI keys can be drained quickly if leaked, leading to high usage costs.",
}
