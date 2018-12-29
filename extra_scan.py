def extras_scan():
    import os
    from termcolor import cprint, colored
    from pathlib import Path

    extras = list()
    persist = list()
    PATH = './data/scripts/'
    PERSIST_SCRIPTS = './data/scripts/persistance'
    decision = input("[ ! ] Please select a path:\n1 . ){} \n2 . ){}\n->".format(PATH, PERSIST_SCRIPTS))
    if decision == '1':
        print("[ + ] Available extras [ + ]")
        for files in os.listdir('./data/scripts/'):
            cprint("[ + ] {} [ + ]".format(files), "white", attrs=['blink', 'bold'])
            for file in files:
                if file.endswith('.py'):
                    extras.extend(file)
        choice = input("Please enter your choice:\n->")
        for index in persist:
            if choice == index:
                cprint("[ + ] You selected: [ + ]\n->{}".format(choice), "blue", attrs=["bold"])
                Path(PATH + choice)

    if decision == '2':
        print("[ + ] Persistance Modules: [ + ]")
        for files in os.listdir('./data/scripts/persistance/'):
            cprint("[ + ] {} [ + ]".format(files), "white", attrs=['blink', 'bold'])
            for file in files:
                if file.endswith(".py"):
                    persist.extend(file)
        choice = input("Please enter your choice:\n->")
        for index in persist:
            if choice == index:
                cprint("[ + ] You selected: [ + ]\n->{}".format(choice), "blue", attrs=["bold"])

if __name__ == "__main__":
    extras_scan()
