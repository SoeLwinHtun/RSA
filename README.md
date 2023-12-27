# Different ways of implementation RSA algorithm

The RSA algorithm is widely used to enable public-key encryption, resulting in secure data storage and transmission, among other benefits. A detailed explanation of the RSA algorithm can be found on [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

This project contains examples of implementing the RSA algorithm using different Python libraries, such as SymPy and cryptography. In real-life applications, the key generation part of the RSA algorithm is more complicated. 

The project is simply for new learners of python as a language or those who interested in encryption algorithms in general. 


## Program Usage

To run the program you need to install sympy, cryptography and pycryptodome modules.
Run the following command. They can be also found on requirements file.

```bash
pip install sympy
pip install cryptography
pip insatll pycryptodome
```

There will be three different implementation of RSA algorithm.

The first one used sympy module and is called rsa_sympy.py
To run the program, execute the following command in your terminal:

```bash
python rsa_sympy.py
```

The program will prompt you with the following menu:

```bash
Choose operation:
1. Encrypt
2. Decrypt
-1. Quit

```

Let's press 1 to perform encryption.

```bash
Enter 1, 2, or -1: 1
Enter the text: apple
Key pair:  (3141793, 17107) (3141793, 996943)
Encrypted text: [2307921, 2197676, 2197676, 1809669, 1003678]
```

Copy the encrypted text and the key pair, The first pair is public key and the second pair is the private key.

Now let's try to revert the cipher text back to plain text.

```bash
Choose operation:
1. Encrypt
2. Decrypt
-1. Quit
Enter 1, 2, or -1: 2
```

To make this program work you need to enter the correct format of input.

The plain text is in list form [ digit, digit, digit ]
The private key pair is in tuple ( digit, digit )

You need to enter correct form otherwise the program will have error.
You can modify the program so that it will catch unwant input.

```bash
Enter the text: [2307921, 2197676, 2197676, 1809669, 1003678]
Enter the private key (comma-separated n,d): (3141793, 996943)
Decrypted text: apple
Choose operation:
1. Encrypt
2. Decrypt
-1. Quit
Enter 1, 2, or -1: -1
Quitting the program.
```

Remember that correct input is absolutely necessary for the program to work as intended.

Now Let's move on to RSA implementation using cryptography module.

This one is different from sympy program since it doesn't have decryption function. 

Since key pair generated with cryptography module is in byte form, the user need to enter correct private key in byte form to decrypt correctly. You can try to add that feature your self too.

Let's run the program.

```bash
python rsa_cryptography.py
```

It will ask for the plain text to encrypt and display the key pair used here for you to save it.
