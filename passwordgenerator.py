import random
import string


letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation


all_in_one = list(letters + digits + symbols)
letters_and_digits = list(letters + digits)
letters_and_symbols = list(letters + symbols)
digits_and_symbols = list(digits + symbols)


option = int(input("""
        Which password option do you want to use:
        1 - Letters and Digits
        2 - Letters and Symbols
        3 - Digits and Symbols
        4 - All in One
"""))

number_of_symbols = int(
    input('Enter number of characters in your password (8-24): '))


def generate_random_password(option, number_of_symbols):
    if option == 1:
        random.shuffle(letters_and_digits)
        password = random.choices(letters_and_digits, k=number_of_symbols)
        return ("".join(password))

    elif option == 2:
        random.shuffle(letters_and_symbols)
        password = random.choices(letters_and_symbols, k=number_of_symbols)
        return ("".join(password))

    elif option == 3:
        random.shuffle(digits_and_symbols)
        password = random.choices(digits_and_symbols, k=number_of_symbols)
        return ("".join(password))

    elif option == 4:
        random.shuffle(all_in_one)
        password = random.choices(all_in_one, k=number_of_symbols)
        return ("".join(password))


print(f"""Your password is: 
       ====================
       {generate_random_password(option, number_of_symbols)}
       ====================
""")
