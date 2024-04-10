import random
import string
import pyperclip  # For copying password to clipboard

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print("Generated Password:", password)

    # Copy to clipboard
    copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").lower() == 'y'
    if copy_to_clipboard:
        pyperclip.copy(password)
        print("Password copied to clipboard.")

if __name__ == "__main__":
    main()
