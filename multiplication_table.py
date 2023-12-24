import pickle
import random
from collections import defaultdict
from datetime import datetime
from colorama import Fore, Back, Style

TABLES = [3, 4, 6, 7, 8, 9]
MUTLIPLES = [3, 4, 5, 6, 7, 8, 9]
FILE_PATH = "old_results.pkl"


class OldResults:
    def __init__(self, path: str = FILE_PATH):
        self.path = path
        self.load_old_results()

    def load_old_results(self):
        try:
            with open(self.path, 'rb') as f:
                results = pickle.load(f)
        except FileNotFoundError:
            results = {}
        results_dict = defaultdict(int, results)
        self.results = results_dict

    def update_results(self, table, multiple, points):
        key = tuple(sorted([table, multiple]))
        self.results[key] += points
        self.save_results()

    def save_results(self):
        with open(self.path, 'wb') as f:
            pickle.dump(self.results, f)


def ask_input_type(prompt: str, input_type: object):
    result = input(prompt + "\n")
    if result.upper() == "Q":
        print(Fore.RESET + "Merci d'avoir joué avec moi 😘")
        exit()
    try:
        return input_type(result)
    except BaseException:
        print(Fore.RED + "Mauvaise saisie ! ! ! ☠️ 💀 👺")
        return ask_input_type(prompt, input_type)


def ask_multiplication(table, multiple):
    start_time = datetime.now()
    result = ask_input_type(Fore.RESET + f"Combien font {table} x {multiple}\n", int)
    total_time = (datetime.now() - start_time).seconds
    if result != table * multiple:
        print(Fore.BLUE + f"{table} x {multiple} = {table * multiple}")
        print(Fore.RED + f"\nTu perds 2 points.\n")

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

                print(
                    Fore.YELLOW + f"C'est la bonne réponse mais tu as mis trop de temps ! 🥴"
                                  f"\nÇa t'as pris {total_time} secondes pour trouver le résultat."
                                  f"\nMalheureusement tu perds {abs(points)} points !\n"
                )
                return points
        print(
            Fore.GREEN + f"Bravo ! 🥳  ️‍🔥"
                         f"\nTu as mis {total_time} secondes pour trouver le résultat."
                         f"\nCela te rapporte {points} points !\n"
        )
        return points


def get_random_table_and_multiple(old_results: dict, tables: list = TABLES, multiples: list = MUTLIPLES):
    choose_old_results = random.randint(1, 3) == 1
    bad_old_results = {key: value for key, value in old_results.items() if value < 0}
    if len(bad_old_results) > 5 and choose_old_results:
        table, multiple = random.choice(list(bad_old_results.keys()))
    else:
        table = random.choice(tables)
        multiple = random.choice(multiples)
    return table, multiple


def main():
    score = 0
    goal = ask_input_type("\nCoucou !\nTu veux jouer en combien de points ?", int)
    while score < goal:
        old_results = OldResults()
        table, multiple = get_random_table_and_multiple(old_results.results)

        input(Fore.RESET + "\nEst ce que tu es prête ?\n")

        points = ask_multiplication(table, multiple)
        old_results.update_results(table, multiple, points)
        score += points

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"\nTu as gagné !!! 🥳🥳🥳\n")


if __name__ == "__main__":
    main()
