def decrypt_caesar(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_cryptanalysis(ciphertext):
    # Brute force through all possible shift values
    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Example Usage:
encrypted_text = "Khoor, Zruog!"
print(f"Encrypted: {encrypted_text}\n")
print("Cryptanalysis Results:")
caesar_cryptanalysis(encrypted_text)
