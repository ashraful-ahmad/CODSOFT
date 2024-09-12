import random
import string

def generate_password(pw_length):
    # Define individual character sets
    lower_chars = string.ascii_lowercase   # Lowercase letters
    upper_chars = string.ascii_uppercase   # Uppercase letters
    digit_chars = string.digits            # Digits
    special_chars = string.punctuation     # Special characters
    
    # Combine all character sets into one pool
    all_chars = lower_chars + upper_chars + special_chars + digit_chars

    # Start building the password with one character from each set to ensure complexity
    password = [
        random.choice(lower_chars),
        random.choice(upper_chars),
        random.choice(digit_chars),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    # (Subtract 4 since we've already picked 4 characters)
    if pw_length > 4:
        password += random.choices(all_chars, k=pw_length - 4)

    # Shuffle the result to make the password even more random
    random.shuffle(password)

    # Join the list into a single string and return the result
    return ''.join(password)

# Let the user set the length of the password
try:
    user_length = int(input("Enter the desired password length (min 6): "))
    if user_length < 6:
        print("Password length should be at least 6 characters.")
    else:
        # Generate the password
        secure_password = generate_password(user_length)
        print(f"Your secure password is: {secure_password}")
except ValueError:
    print("Please enter a valid number.")