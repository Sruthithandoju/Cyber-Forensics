#!/usr/bin/env python3
import sys

def xor_decrypt(encrypted_bytes, key):
    """Decrypt message using XOR with the given key"""
    key_bytes = [ord(c) for c in key]
    decrypted = ""
    for i in range(len(encrypted_bytes)):
        decrypted += chr(encrypted_bytes[i] ^ key_bytes[i % len(key)])
    return decrypted

def extract_hex_data(filename, start_offset, length):
    """Extract data from file at given offset"""
    with open(filename, 'rb') as f:
        f.seek(start_offset)
        data = f.read(length)
    return data

if len(sys.argv) != 4:
    print("Usage: python3 solve.py <image_file> <offset> <key>")
    sys.exit(1)

image_file = sys.argv[1]
offset = int(sys.argv[2], 0)  # Allow for hex input like 0xA4D0
key = sys.argv[3]

# Try with the length of the visible hex dump (37 bytes)
data_length = 37  # You may need to adjust this

# Extract the encrypted data from the image
encrypted_bytes = extract_hex_data(image_file, offset, data_length)

# Decrypt the message
decrypted = xor_decrypt(encrypted_bytes, key)

print("Extracted encrypted data:", encrypted_bytes.hex())
print("Decrypted message:", decrypted)
