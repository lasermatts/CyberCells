# logo.py

from colorama import Fore, init

init(autoreset=True)

def print_logo():
    logo = """
 
 \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 --o-|C|Y|B|E|R|-|C|E|L|L|S|-o--
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    """
    print(Fore.RED + logo)
