from nacl.signing import SigningKey
import base64, os

sk = SigningKey.generate()
vk = sk.verify_key

private_hex = sk.encode().hex()
public_b64 = base64.b64encode(vk.encode()).decode()

print(private_hex)
print(f"ed25519: {public_b64}")

env_path = ".env"
env_lines = [
    f"PRIVATE_KEY={private_hex}",
    f"PUBLIC_KEY={public_b64}"
]

with open(env_path, "w", encoding="utf-8") as f:
    f.write("\n".join(env_lines) + "\n")

print(os.path.abspath(env_path))
