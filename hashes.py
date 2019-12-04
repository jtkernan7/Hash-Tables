import time
import hashlib
import bcrypt 

key = b"hello"

print (hashlib.sha256(key).hexdigest())

def djb2(key):
    hash_value = 5381


    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

print(djb2(key))

djb2key = djb2(key)

print(f"sha256 key: {int(sha256) % 10}")
print(f"djb2 key: {djb2key % 10}")