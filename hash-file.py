#!/usr/bin/python3
import hashlib as hlib

def hash_file(filename):
    h = hlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return  h.hexdigest()     

message = hash_file("README.md");
print(message)
