import random
import string

def generate_password():
    print("🔐 Password Generator")
    print("----------------------")
    
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return

        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_chars = lowercase + uppercase + digits + symbols

        # Ensure password contains at least one of each type
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols),
        ]

        # Fill the rest of the password length
        password += random.choices(all_chars, k=length - 4)

        # Shuffle to prevent predictable order
        random.shuffle(password)

        # Convert list to string
        final_password = ''.join(password)

        print("Generated Password:", final_password)
    
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    generate_password()
