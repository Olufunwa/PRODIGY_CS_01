def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():  # Check if the character is a letter
            shift = key % 26
            if letter.islower():
                start = ord('a')
            else:
                start = ord('A')
            new_index = (ord(letter) - start + shift) % 26 + start
            ciphertext += chr(new_index)
        else:
            ciphertext += letter  # Keep non-alphabet characters as is
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():  # Check if the character is a letter
            shift = key % 26
            if letter.islower():
                start = ord('a')
            else:
                start = ord('A')
            new_index = (ord(letter) - start - shift) % 26 + start
            plaintext += chr(new_index)
        else:
            plaintext += letter  # Keep non-alphabet characters as is
    return plaintext

def main():
    print("Welcome to the Caesar Cipher Program!")

    while True:
        choice = input("Would you like to encrypt or decrypt? (Enter 'encrypt' or 'decrypt', or 'exit' to quit): ").lower()

        if choice == 'encrypt':
            key = int(input("Enter the shift value (1-25): "))
            text = input("Enter the text: ")
            encrypted_text = encrypt(text, key)
            print(f'Encrypted Text: {encrypted_text}')
        
        elif choice == 'decrypt':
            key = int(input("Enter the shift value (1-25): "))
            text = input("Enter the text: ")
            decrypted_text = decrypt(text, key)
            print(f'Decrypted Text: {decrypted_text}')

        elif choice == 'exit':
            print("Thank you for using the Caesar Cipher Program!")
            break
        
        else:
            print("Invalid option. Please enter 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
