from random import choice, shuffle

NUMERIC = "0123456789"
LETTERS = "abcdefghijklmnopqrstuvwxyz"
BIG_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOL = "!#%$&*+-=?@^_"

def generate_password(length: int, chars: list) -> str:
    psw = [choice(category) for category in chars]

    remaining_length = length - len(psw)
    if remaining_length > 0:
        psw.extend([choice("".join(chars)) for _ in range(remaining_length)])
    shuffle(psw)

    return "".join(psw)

def text_valid(message: str, correct_answ: list = ["Yes", "No"]) -> str:
    message = message.strip().capitalize()

    while message not in correct_answ:
        print("incorrect input")
        message = input("please try again: ").strip().capitalize()

    return message

def numb_valid(message: str) -> int:
    while not message.isdigit() or int(message) < 0:
        print("Incorrect input")
        message = input("Please try again enter number: ")

    return int(message)   

def main():
    chars = list()

    #считывание пользовательских данных
    quest_num_pass = text_valid(input("should I include numbers in the password?(Yes/No) "))

    quest_biglt_pass = text_valid(input("should I include uppercase letters?(Yes/No) ")) 

    quest_lt_pass = text_valid(input("should I include lowercase letters?(Yes/No) "))

    quest_sym_pass = text_valid(input("should I include symbols?(Yes/No) "))

    if quest_num_pass == "Yes":
        chars.append(NUMERIC)

    if quest_biglt_pass == "Yes":
        chars.append(BIG_LETTERS)

    if quest_lt_pass == "Yes":
        chars.append(LETTERS)

    if quest_sym_pass == "Yes":
        chars.append(SYMBOL)
    
    if len(chars) == 0:
        print("Select at least one category for the password")

        return main()
    
    num_pas_gen = numb_valid(input("enter the number of passwords to generate: "))

    length = numb_valid(input("enter the length of one password: ")) 

    if length < len(chars):
        print("The password length must be greater or equal than the number of selected categories")

        return main()
    
    for _ in range(num_pas_gen):
        print(generate_password(length, chars))
        print()

main()