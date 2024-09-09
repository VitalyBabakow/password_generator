from random import choice, shuffle

num = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!#%$&*+-=?@^_"

def generate_password(length: int, chars: str) -> str:
    psw = ""
    chars = list(chars)
    shuffle(chars)
    for _ in range(length):
        psw = psw + choice(chars)

    return psw

def text_valid(message: str, correct_answ: list = ["Yes", "No"]) -> str:
    while message not in correct_answ:
        print("incorrect input")
        message = input("please try again: ")

    return message

def numb_valid(message: str) -> int:
    while not message.isdigit():
        print("Incorrect input")
        message = input("Please try again enter number: ")

    return int(message)   

def main():
    chars = ""

    #считывание пользовательских данных
    num_pas_gen = numb_valid(input("enter the number of passwords to generate: "))

    length = numb_valid(input("enter the length of one password: ")) 

    quest_num_pass = text_valid(input("should I include numbers in the password?(Yes/No) "))

    quest_biglt_pass = text_valid(input("should I include uppercase letters?(Yes/No) ")) 

    quest_lt_pass = text_valid(input("should I include lowercase letters?(Yes/No) "))

    quest_sym_pass = text_valid(input("should I include symbols?(Yes/No) "))


    if quest_num_pass == "Yes":
        chars += num

    if quest_biglt_pass == "Yes":
        chars += big_letters

    if quest_lt_pass == "Yes":
        chars += letters

    if quest_sym_pass == "Yes":
        chars += symbol

    for _ in range(num_pas_gen):
        print(generate_password(length, chars))
        print()

main()
