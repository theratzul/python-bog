#!/usr/bin/python3

from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

nonce, ciphertext, tag = encrypt(input("Ebter a message: "))
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print("Message is corrupted")
else:
    printf('Plain text: {plaintext}')