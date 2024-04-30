def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text):
    decrypted_texts = []
    for shift in range(26):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def main():
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    if choice == 'E':
        text = input("Enter the text you want to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted:", encrypted_text)
    elif choice == 'D':
        text = input("Enter the text you want to decrypt: ")
        decrypted_texts = caesar_decrypt(text)
        print("Possible Decryptions:")
        for i, decrypted_text in enumerate(decrypted_texts):
            print(f"{i+1}. {decrypted_text}")
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
