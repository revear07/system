def encrypt_substitution(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            offset = ord ('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result +=char
    return result
def decrypt_substitution(ciphertext, shift):
    return encrypt_substitution(ciphertext, -shift)

# Example Usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = encrypt_substitution(plaintext, shift)
decrypted_text = decrypt_substitution(encrypted_text, shift)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
