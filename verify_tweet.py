from nacl.signing import VerifyKey
import base64

env = {}
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()

if "PUBLIC_KEY" not in env:
    raise SystemExit("PUBLIC_KEY missing from .env")

PUBLIC_KEY_B64 = env["PUBLIC_KEY"]

print("Paste tweet and press Enter twice:")
tweet_lines = []
while True:
    line = input()
    if not line:
        break
    tweet_lines.append(line)

if not tweet_lines:
    raise SystemExit("No tweet entered")

TWEET = "\n".join(tweet_lines)

lines = TWEET.splitlines()
if len(lines) < 2 or not lines[-1].startswith("#sig:"):
    raise SystemExit("bad tweet format")

msg_text = "\n".join(lines[:-1])
sig_b64 = lines[-1].split(":", 1)[1]

vk = VerifyKey(base64.b64decode(PUBLIC_KEY_B64))

try:
    vk.verify(msg_text.encode("utf-8"), base64.b64decode(sig_b64))
    print("valid")
except Exception:
    print("invalid")
