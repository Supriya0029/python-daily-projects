##__ DAY 07 OF SIMPLE PYTHON PROJECT__##

import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("Simple password generator ")
length = int(input("Enter password length :"))
print("Your password is:", generate_password(length) )
