from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

#rsa.generate_private_key is used to generate a private key with a given public exponent (65537) and key size (2048 bits).
#The corresponding public key is obtained from the private key.
#The keys are then serialized to PEM format, which is a common format for storing RSA keys.

def generate_keypair_cryptography():
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
    plaintext = private_key.decrypt(
        ciphertext,
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
    public_key, private_key = generate_keypair()

    while True:
        choice = get_user_choice()

        if choice == 1:  # Encrypt
            plaintext = get_text()
            private_key_c, public_key_c = generate_keypair_cryptography()
            ciphertext_c = encrypt_rsa_cryptography(plaintext_c, public_key_c)
            print("Encrypted text:", ciphertext_c)
        elif choice == -1:  # Quit
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()

private_key_c, public_key_c = generate_keypair_cryptography()
plaintext_c = "Hello, RSA!"
ciphertext_c = encrypt_rsa_cryptography(plaintext_c, public_key_c)
decrypted_text_c = decrypt_rsa_cryptography(ciphertext_c, private_key_c)

print("Original Text:", plaintext_c)
print("Ciphertext:", ciphertext_c)
print("Decrypted Text:", decrypted_text_c)
