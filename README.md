# CYB 371 - Hashing Assignment

A Python program that demonstrates hashing using the standard `hashlib` library.

## Student Details
- **Name:** IBIZUGBE MICHAEL GREGORY
- **Matric No:** 24/14703
- **Department:** CYBER SECURITY
- **Level:** 300
- **Course:** CUL-CYB371

## What the program does
1. Hashes a **word** (`cybersecurity`)
2. Hashes a **sentence**
3. Hashes a **paragraph** of not less than five (5) lines

For each input, the program prints hashes using three algorithms:
**SHA-256**, **SHA-1**, and **MD5**.

## How to run
```bash
python3 hash_text.py
```

No installation is required; `hashlib` is part of the Python standard library.

## Files
- `hash_text.py` - the hashing program

## Note on hashing
A hash is a one-way function: the same input always produces the same fixed-length
digest, but the input cannot be recovered from the digest. Even a one-character change
completely changes the output (the avalanche effect), which is why hashing is used for
integrity checks and password storage in cyber security.
