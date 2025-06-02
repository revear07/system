import hashlib

def sha1_hash(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode())
    return sha1.hexdigest()

# Example usage
message = "HELLO"
hash_value = sha1_hash(message)

print("Original Message:", message)
print("SHA-1 Hash:", hash_value)
