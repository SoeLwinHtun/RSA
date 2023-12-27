from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def encrypt_rsa_cryptography(text, public_key):
    public_key = serialization.load_pem_public_key(public_key)
    ciphertext = public_key.encrypt(
        text.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_rsa_cryptography(ciphertext, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None)

    # Convert the byte-like object to a list of integers
    ciphertext_list = list(ciphertext)

    plaintext = private_key.decrypt(
        ciphertext_list,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')


def get_text():
    text = input("Enter the text: ")
    return text

def get_user_choice():
    while True:
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("-1. Quit")
        choice = input("Enter 1, 2, or -1: ")

        if choice in ['1', '2', '-1']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or -1.")

def main():
    private_key, public_key = generate_keypair()

    while True:
        choice = get_user_choice()

        if choice == 1:  # Encrypt
            plaintext = get_text()
            ciphertext = encrypt_rsa_cryptography(plaintext, public_key)
            print("Key pair:", public_key, private_key)
            print("Encrypted text:", ciphertext)
        elif choice == 2:  # Decrypt
            ciphertext = input("Enter the ciphertext: ")
            plaintext = decrypt_rsa_cryptography(ciphertext, private_key)
            print("Decrypted text:", plaintext)
        elif choice == -1:  # Quit
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()
