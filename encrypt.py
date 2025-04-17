#!/usr/bin/env python3

import sys

def xor_encrypt(message, key):
    """Encrypt message using XOR with the given key"""
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted

def string_to_hex(text):
    """Convert text to hex representation"""
    return ' '.join([hex(ord(c))[2:].zfill(2) for c in text])

if len(sys.argv) != 3:
    print("Usage: python3 encrypt.py <message> <key>")
    sys.exit(1)

message = sys.argv[1]
key = sys.argv[2]

encrypted = xor_encrypt(message, key)
hex_result = string_to_hex(encrypted)

print("Original message:", message)
print("Encrypted (ASCII):", encrypted)
print("Encrypted (HEX):", hex_result)
print("\nHex values to insert in your image:")
print(hex_result.replace(' ', ''))
