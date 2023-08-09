# logo.py

from colorama import Fore, init

init(autoreset=True)

def print_logo():
    logo = """
 +-+-+-+-+-+-+-+-+-+-+-+
 |C|Y|B|E|R|-|C|E|L|L|S|
 +-+-+-+-+-+-+-+-+-+-+-+
    """
    print(Fore.CYAN + logo)
