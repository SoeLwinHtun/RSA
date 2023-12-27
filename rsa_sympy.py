import sympy
import ast

#generating key in RSA algorithm is the main part and the key pair could be generated using different methods

#Two random prime numbers (p and q) are generated.
#The modulus n is calculated as the product of p and q.
#Euler's totient function phi is calculated based on p and q.
#A public exponent e is randomly chosen such that it is coprime with phi.
#The private exponent d is calculated as the modular inverse of e modulo phi.
#The public key is (n, e) and the private key is (n, d).

def generate_keypair():
    p = sympy.randprime(10**3, 10**4)
    q = sympy.randprime(10**3, 10**4)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = sympy.randprime(2, phi)
    while sympy.gcd(e, phi) != 1:
        e = sympy.randprime(2, phi)
    
    d = sympy.mod_inverse(e, phi)
    
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

#For each integer in the encrypted text, it is raised to the power of the private exponent (d) modulo the modulus (n).
#The result is converted back to a character using chr and joined to form the decrypted text.

def encrypt_rsa(text, public_key):
    n, e = public_key
    encrypted_text = [pow(ord(char), e, n) for char in text]
    return encrypted_text

def decrypt_rsa(encrypted_text, private_key):
    n, d = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
    return decrypted_text

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
            encrypted_text = encrypt_rsa(plaintext, public_key)
            print("Key pair: ",public_key,private_key)
            print("Encrypted text:", encrypted_text)
        elif choice == 2:  # Decrypt
            encrypted_text = get_text()

            #change the cipher text to the list
            encrypted_text_list = ast.literal_eval(encrypted_text)

            # Ask the user for the private key
            private_key_input = input("Enter the private key (comma-separated n,d): ")

            #convert it to tuple form

            private_key_input_tuple = ast.literal_eval(private_key_input)
            decrypted_text = decrypt_rsa(encrypted_text_list, private_key_input_tuple)

            print("Decrypted text:", decrypted_text)
        elif choice == -1:  # Quit
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()