import argparse
import base64
from nacl.signing import SigningKey
from pathlib import Path


def load_env(path):
    env = {}
    if not Path(path).exists():
        raise SystemExit(f"{path} not found. Run gen_key.py first.")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def main():
    parser = argparse.ArgumentParser(
        description="Sign a tweet with your Ed25519 private key."
    )
    parser.add_argument(
        "-m", "--message",
        help="Tweet text to sign. If omitted, you’ll be prompted to type it."
    )
    parser.add_argument(
        "--env",
        default=".env",
        help="Path to .env file containing PRIVATE_KEY (default: .env)."
    )
    args = parser.parse_args()

    env = load_env(args.env)

    if "PRIVATE_KEY" not in env:
        raise SystemExit("PRIVATE_KEY missing from .env")

    msg = args.message or input("Enter tweet text: ").strip()
    if not msg:
        raise SystemExit("Empty tweet, nothing to sign.")

    sk = SigningKey(bytes.fromhex(env["PRIVATE_KEY"]))
    signed = sk.sign(msg.encode("utf-8"))
    sig_b64 = base64.b64encode(signed.signature).decode("ascii")

    print(msg)
    print(f"//sig:{sig_b64}")


if __name__ == "__main__":
    main()