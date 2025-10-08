
from colorama import Fore, Style, init

init(autoreset=True)

try:
    with open("sample.txt", "r") as file:
        print(Fore.MAGENTA + "Reading file content:\n")
        for i, line in enumerate(file, start=1):
            print(Fore.GREEN + f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(Fore.RED + "Error:" + Fore.RESET + f" The file {Fore.CYAN}'sample.txt'{Fore.RESET} was not found.")

