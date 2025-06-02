from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_and_decrypt_aes_example():
    # Generate a 128-bit (16 bytes) key
    key = get_random_bytes(16)

    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt
    plaintext = b'This is a sample plaintext'

    # Pad the plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext, AES.block_size)

    ciphertext = cipher.encrypt(padded_plaintext)
    print(f'Plaintext: {plaintext}')
    print(f'Ciphertext: {ciphertext.hex()}')

    # Decrypt
    decrypted_text = cipher.decrypt(ciphertext)

    # Unpad the decrypted plaintext
    unpadded_decrypted_text = unpad(decrypted_text, AES.block_size)

    print(f'Decrypted Text: {unpadded_decrypted_text.decode()}')

if __name__ == "__main__":
    encrypt_and_decrypt_aes_example()
