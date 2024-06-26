import string
import random

def generate_password(number):
    # Creating the lists which contain uppercase and lowercase letters, digits, and punctuation
    group1 = list(string.ascii_uppercase)
    group2 = list(string.ascii_lowercase)
    group3 = list(string.digits)
    group4 = list(string.punctuation)

    # Shuffling the elements in groups
    random.shuffle(group1)
    random.shuffle(group2)
    random.shuffle(group3)
    random.shuffle(group4)

    # Calculating the percentage of each group
    first_part = round(number * (30 / 100))
    second_part = round(number * (20 / 100))

    # Generating the password
    password = []
    for i in range(first_part):
        password.append(group1[i])
        password.append(group2[i])

    for i in range(second_part):
        password.append(group3[i])
        password.append(group4[i])

    random.shuffle(password)  # Shuffling the password again to be satisfy
    real_password = "".join(password)  # Joining the characters in the list to form the password
    return real_password