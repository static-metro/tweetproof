import argparse
import base64
import os
from pathlib import Path
from nacl.signing import SigningKey


def main():
    parser = argparse.ArgumentParser(
        description="Generate an Ed25519 keypair and write it to a .env file."
    )
    parser.add_argument(
        "--out",
        default=".env",
        help="Path to output file (default: .env)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing file without asking"
    )
    args = parser.parse_args()

    env_path = Path(args.out)

    if env_path.exists() and not args.force:
        confirm = input(f"{env_path} already exists. Overwrite? (y/n): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            raise SystemExit(0)

    sk = SigningKey.generate()
    vk = sk.verify_key

    private_hex = sk.encode().hex()
    public_b64 = base64.b64encode(vk.encode()).decode()

    print(f"Private key (keep secret): {private_hex}")
    print(f"Public key (put in bio): ed25519: {public_b64}")

    env_lines = [
        f"PRIVATE_KEY={private_hex}",
        f"PUBLIC_KEY={public_b64}"
    ]

    with open(env_path, "w", encoding="utf-8") as f:
        f.write("\n".join(env_lines) + "\n")

    print(f"Wrote keys to {env_path.resolve()}")


if __name__ == "__main__":
    main()
