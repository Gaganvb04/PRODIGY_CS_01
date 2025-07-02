import string

def encryption(plain_text, shift_key):
    chars = string.printable
    result = ""
    for char in plain_text:
        if char in chars:
            idx = chars.index(char)
            new_idx = (idx + shift_key) % len(chars)
            result += chars[new_idx]
        else:
            result += char
    return result

def decryption(cipher_text, shift_key):
    chars = string.printable
    result = ""
    for char in cipher_text:
        if char in chars:
            idx = chars.index(char)
            new_idx = (idx - shift_key) % len(chars)
            result += chars[new_idx]
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher===")
    wanna_end = False

    while not wanna_end:
        what_to_do = input("\nType 'encrypt' for encryption, type 'decrypt' for decryption:\n").strip().lower()

        if what_to_do == 'encrypt':
            text = input("Type your message:\n")
            try:
                shift = int(input("Enter shift key:\n"))
                encrypted = encryption(plain_text=text, shift_key=shift)
                print(f"\nEncrypted Message: {encrypted}")
            except ValueError:
                print("Shift must be a number.")
                continue

        elif what_to_do == 'decrypt':
            text = input("Type your message:\n")
            try:
                shift = int(input("Enter shift key:\n"))
                decrypted = decryption(cipher_text=text, shift_key=shift)
                print(f"\nDecrypted Message: {decrypted}")
            except ValueError:
                print("Shift must be a number.")
                continue

        else:
            print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
            continue
        # Ask to continue
        play_again = input("\nType 'yes' to continue, type 'no' to exit:\n").strip().lower()
        if play_again in ['no', 'n']:
            wanna_end = True
            print("Have a nice day! Bye...")

if __name__ == "__main__":
    main()
