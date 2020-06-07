from termcolor import cprint
from random import randint


def printLogo():
    logo = """
     ▄▄▄       ██▓     ▄▄▄▄   ▓█████  ██▀███  ▄▄▄█████▓
    ▒████▄    ▓██▒    ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒
    ▒██  ▀█▄  ▒██░    ▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░
    ░██▄▄▄▄██ ▒██░    ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░
     ▓█   ▓██▒░██████▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒  ▒██▒ ░
     ▒▒   ▓▒█░░ ▒░▓  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░
      ▒   ▒▒ ░░ ░ ▒  ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░    ░
      ░   ▒     ░ ░    ░    ░    ░     ░░   ░   ░
          ░  ░    ░  ░ ░         ░  ░   ░
                            ░
                            
    """


    choice = randint(1, 3)
    color = ''
    if choice == 1:
        color = "blue"
    elif choice == 2:
        color = "red"
    elif choice == 3:
        color = "red"

    cprint(f"{logo}", color, attrs=["bold", "dark"])
    cprint("Gr33tz: Chef, Robert Ross(Root), Sam", color, attrs=["bold", "dark"])
    cprint("R3p0: https://github.com/oldkingcone/Albert", color, attrs=["bold", "dark"])
    cprint("H4ppy H4ck1ng!", color, attrs=["bold", "dark"])