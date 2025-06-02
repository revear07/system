import hashlib

def md5_hash(data):
    # Create an MD5 hash object
    md5_hash_object = hashlib.md5()

    # Update the hash object with the input data
    md5_hash_object.update(data.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    md5_hex_digest = md5_hash_object.hexdigest()

    return md5_hex_digest

if __name__ == "__main__":
    # Example usage
    input_data = input("Enter the data to hash using MD5: ")
    md5_result = md5_hash(input_data)
    print(f"MD5 hash of '{input_data}': {md5_result}")
