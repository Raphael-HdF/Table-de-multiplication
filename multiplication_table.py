import random
from datetime import datetime
from colorama import Fore, Back, Style


tables = [3, 4, 6, 7, 8, 9]
mutliples = [3, 4, 5, 6, 7, 8, 9]


def ask_input_type(prompt:str, input_type:object):
    result = input(prompt)
    if result.upper() == "Q":
        print("Merci d'avoir joué avec moi 😘")
    try:
        return input_type(result)
    except BaseException:
        print(Fore.RED + "Mauvaise saisie ! ! ! ☠️ 💀 👺")
        return ask_input_type(prompt, input_type)


def ask_multiplication(table, multiple):
        start_time = datetime.now()
        result = ask_input_type(f"Combien font {table} x {multiple}\n", int)
        total_time = datetime.now() - start_time
        if result != table * multiple:
            print(Fore.RED + f"{table} x {multiple} = {table * multiple}"
                             f"\nTu perds 2 points")
            return -2
        else:
            match total_time:
                case _ if total_time <= 5:
                    points = 2
                case _ if total_time <= 10:
                    points = 1
                case _ if total_time <= 15:
                    points = 0
                case _:
                    points = -1

            print(Fore.GREEN + f"Bravo !"
                               f"\n tu as mis {total_time} secondes pour trouver le résultat")


def init_multiplication_game():

    score
def main():

    while True:
        table = random.choice(tables)
        multiple = random.choice(mutliples)

        result = input(f"Combien font {table} x {multiple}\n")
        if result.lower() == "q":
            exit()
        if result.isnumeric():
            res = int(result)

            if res == table * multiple:
                print('Bravo !\n\n')
            else:
                print(f'Le résultat est => {table} x {multiple} = {multiple * table}\n\n')
        else:
            print(f'Tape des chiffres\n\n')


if __name__ == "__main__":
    main()
