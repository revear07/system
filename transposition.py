def encrypt(text, key):
    # Remove spaces and convert text to uppercase
    text = text.replace(" ", "").upper()

    # Calculate the number of rows required based on the key
    rows = len(text) // key
    if len(text) % key != 0:
        rows += 1

    # Create a 2D matrix to store the characters
    matrix = [[' ' for _ in range(key)] for _ in range(rows)]

    # Fill the matrix with characters from the plaintext
    index = 0
    for i in range(rows):
        for j in range(key):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    # Read the matrix column-wise to get the ciphertext
    ciphertext = ""
    for j in range(key):
        for i in range(rows):
            ciphertext += matrix[i][j]

    return ciphertext


def decrypt(ciphertext, key):
    # Calculate the number of rows required based on the key
    rows = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        rows += 1

    # Create a 2D matrix to store the characters
    matrix = [[' ' for _ in range(key)] for _ in range(rows)]

    # Fill the matrix with characters from the ciphertext
    index = 0
    for j in range(key):
        for i in range(rows):
            if index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    # Read the matrix row-wise to get the plaintext
    plaintext = ""
    for i in range(rows):
        for j in range(key):
            plaintext += matrix[i][j]

    return plaintext

# Example usage
plaintext = "Hello, World!"
key = 4

# Encryption
cipher_text = encrypt(plaintext, key)
print("Encrypted:", cipher_text)

# Decryption
decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
