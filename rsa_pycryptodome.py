from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#RSA.generate(2048) generates a new RSA key pair with a key size of 2048 bits.
#The private key is exported in the default format.
#The public key is obtained from the private key using key.publickey() and then exported.

def generate_keypair_pycryptodome():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa_pycryptodome(text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(text.encode('utf-8'))
    return ciphertext

def decrypt_rsa_pycryptodome(ciphertext, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext

def get_text():
    text = input("Enter the text: ")
    return text

def main():          
    private_key, public_key = generate_keypair_pycryptodome()
    plaintext = get_text()
    ciphertext = encrypt_rsa_pycryptodome(plaintext, public_key)

    print("Encryption completed, the cipher text is :\n", ciphertext)
    print("The Key pair used here is : \n",public_key,private_key)  
# Example usage
    
if __name__ == "__main__":
    main()