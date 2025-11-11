from nacl.signing import SigningKey
import base64, sys

env = {}
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()

if "PRIVATE_KEY" not in env:
    raise SystemExit("PRIVATE_KEY missing from .env")

if len(sys.argv) > 1:
    msg = " ".join(sys.argv[1:]).strip()
else:
    msg = input("Enter tweet text: ").strip()

if not msg:
    raise SystemExit(0)

sk = SigningKey(bytes.fromhex(env["PRIVATE_KEY"]))
signed = sk.sign(msg.encode("utf-8"))
sig_b64 = base64.b64encode(signed.signature).decode("ascii")

print(msg)
print(f"//sig:{sig_b64}")
