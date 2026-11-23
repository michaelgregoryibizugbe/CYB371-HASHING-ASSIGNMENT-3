"""
CYB 371 - Data Mining and Data Warehousing
Assignment: Hashing with Python
Author: IBIZUGBE MICHAEL GREGORY
Matric No: 24/14703
Department: CYBER SECURITY
Level: 300
Course: CUL-CYB371

This program demonstrates hashing:
1) Hash a word
2) Hash a sentence
3) Hash a paragraph of not less than five (5) lines

It uses Python's built-in hashlib library (SHA-256, SHA-1, MD5).
No installation required: hashlib is part of the Python standard library.
"""
import hashlib


def hash_text(text: str, algorithm: str = "sha256") -> str:
    """Return the hexadecimal hash digest of the given text."""
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def show(title: str, text: str):
    """Display the input and its hashes using several algorithms."""
    print("=" * 70)
    print(title)
    print("-" * 70)
    print(f"Input:\n{text}")
    print("-" * 70)
    for algorithm in ("sha256", "sha1", "md5"):
        digest = hash_text(text, algorithm)
        print(f"{algorithm.upper()} ({len(digest) * 4} bits):")
        print(f"  {digest}")
    print("=" * 70)
    print()


def main():
    # 1) Hash a word
    word = "cybersecurity"
    show("1) HASH A WORD", word)

    # 2) Hash a sentence
    sentence = "Data mining helps cyber security analysts detect threats."
    show("2) HASH A SENTENCE", sentence)

    # 3) Hash a paragraph of not less than five (5) lines
    paragraph = (
        "Hashing is a one-way mathematical function that converts data of any\n"
        "size into a fixed-length string of characters called a digest.\n"
        "It is widely used in cyber security to verify file integrity, store\n"
        "passwords safely, and support digital signatures. Even a tiny change\n"
        "in the input produces a completely different hash, a property known\n"
        "as the avalanche effect. This makes hashing a vital tool for\n"
        "detecting tampering and maintaining data integrity."
    )
    line_count = len(paragraph.splitlines())
    show(f"3) HASH A PARAGRAPH ({line_count} LINES)", paragraph)


if __name__ == "__main__":
    main()
