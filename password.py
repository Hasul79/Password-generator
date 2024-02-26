import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

password_length = 12
print("Generated Password:", generate_password(password_length))
