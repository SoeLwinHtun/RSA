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

To run the program, execute the following command in your terminal:

```bash
python rsa_sympy.py
```
or

```bash
python rsa_cryptography.py
```

```bash
python rsa_pycryptodome.py
```

The name of the file will be different based on which method you want to try.

The program will prompt you with the following menu:

```bash
Choose operation:
1. Encrypt
2. Decrypt
-1. Quit
Enter 1, 2, or -1: 1
Enter the text: apple
Key pair:  (3141793, 17107) (3141793, 996943)
Encrypted text: [2307921, 2197676, 2197676, 1809669, 1003678]
Choose operation:
1. Encrypt
2. Decrypt
-1. Quit
Enter 1, 2, or -1: 2
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
