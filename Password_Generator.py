#Password Generator
import random
import string

print("===================================")
print("   SIMPLE PASSWORD GENERATOR")
print("   Oasis Infobyte Project")
print("===================================")

def generate_password(length):
    # check minimum length
    if length < 4:
        return "❌ Password length should be at least 4 characters."

    # character sets
    letters = string.ascii_letters   # a-z + A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation      # special characters

    # ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # combine all characters
    all_chars = letters + digits + symbols

    # fill remaining characters
    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    # shuffle for randomness
    random.shuffle(password)

    # convert list to string
    return "".join(password)


# MAIN PROGRAM (VS Code friendly input loop)
while True:
    try:
        print("\n-----------------------------------")
        length = int(input("Enter password length (or 0 to exit): "))

        if length == 0:
            print("👋 Exiting program. Stay secure!")
            break

        result = generate_password(length)
        print("🔐 Generated Password:", result)

    except ValueError:
        print("⚠️ Please enter a valid number.")