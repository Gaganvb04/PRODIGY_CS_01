# PRODIGY_CS_01
Task-01 Caesar Cipher by using python
# Caesar Cipher (All Printable Characters)

This Python program implements a Caesar Cipher that works with **all printable ASCII characters**, not just letters. It allows the user to **encrypt or decrypt** messages using a shift key, and it loops until the user chooses to exit.

## Features

- Encrypt and decrypt any text using a Caesar Cipher
- Supports all printable characters (letters, digits, symbols, whitespace)
- Repeats until the user decides to quit
- Simple and interactive command-line interface
- Graceful error handling for invalid inputs

## How It Works

The Caesar Cipher works by shifting each character in the message by a specified number of positions in the `string.printable` character set. Decryption reverses this process.

Example:
=== Caesar Cipher===

Type 'encrypt' for encryption, type 'decrypt' for decryption:
encrypt
Type your message:
Gagan V B@123
Enter shift key:
8

Encrypted Message: Oioiv2$2J|9ab

Type 'yes' to continue, type 'no' to exit:
yes

Type 'encrypt' for encryption, type 'decrypt' for decryption:
decrypt
Type your message:
Oioiv2$2J|9ab
Enter shift key:
8

Decrypted Message: Gagan V B@123

Type 'yes' to continue, type 'no' to exit:
no
Have a nice day! Bye...

## How to Run

1. **Clone this repository** or download the `.py` file.

   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Run the script using Python:**

python CaesarCipher.py

**Requirements**
Python 3.x

No external libraries required — uses only Python's standard string module.

**Author**
Gagan V B
https://github.com/Gaganvb04

**License**
This project is open source and available under the MIT License.

### To Use:
1. Save this as a file called `README.md` in your project folder.
2. Replace:
   - `your-username` with your actual GitHub username
   - `your-repo-name` with the repository name
   - `Your Name` with your full name or GitHub name

**Let me know if you want:**
- A version with screenshots
- An example encrypted/decrypted text comparison
- Git commands to push this to GitHub step by step