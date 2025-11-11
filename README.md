# tweetproof

A minimal cryptographic signing system for tweets.  
This lets you **prove that a tweet actually came from you** — without relying on any centralized verification system.

---

## 🌐 Concept

Each tweet is signed locally using an **Ed25519 private key**, producing a short Base64 signature that fits inside the tweet itself:

```md
hello world
//sig:KZcOq9pHk0q8wq1w...etc...
```

Your **public key** (in your Twitter bio) can be used by anyone to verify that the tweet was written by you.

Example bio line:

```md
ed25519: UohHSwvYySRbaqUkirG6jHgNOJnM+x5AgA4XD0E6nqY=
```

Anyone can take your tweet text and signature, use your public key, and confirm authenticity with a verifier.

---

## ⚙️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/static-metro/tweetproof.git
   cd tweetproof
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Generate your Ed25519 keypair:

   ```bash
   python gen_key.py
   ```

   This creates a `.env` file with:

   ```bash
   PRIVATE_KEY=...
   PUBLIC_KEY=...
   ```

   Add the public key (from `.env`) to your Twitter bio in this format:

   ```md
   ed25519: YOUR_PUBLIC_KEY
   ```

4. Sign tweets:

   ```bash
   python sign_tweet.py
   ```

   Output:

   ```md
   testing this out
   //sig:jo/SrSsF4M8gCCu0KXKXw5QS236BoNkx0LfntrQsIM/N1igCKVot/H9pI+rvCs5c...
   ```

   Paste that **exactly** into Twitter.

5. Verify tweets:

   ```bash
   python verify_tweet.py
   ```

   Paste the tweet (including the `//sig:` line) and hit Enter twice.  
   You’ll see:

   ```md
   valid
   ```

   or:

   ```md
   invalid
   ```

---

## 🔒 What This Proves

Anyone can verify:

- The tweet was signed by the same key listed in your bio.
- The tweet text hasn’t been changed since signing.

No one can fake your signature without your private key.

---

## 🧠 Philosophy

The goal is decentralized authorship proof — no corporate checkmark, no server, no blockchain.  
Just a **mathematically verifiable identity**, right there in your bio.

---

## 🧩 Dependencies

Listed in `requirements.txt`

---

## 📜 License

MIT License. Use it, fork it, remix it — just don’t lose your private key.
