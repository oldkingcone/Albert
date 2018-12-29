#this file is still being developed.

def extras_scan():
    import os
    from termcolor import cprint
    extras = list()
    persist = list()
    print("[ + ] Available extras [ + ]")
    for files in os.listdir('./data/scripts/'):
        cprint("[ + ] {} [ + ]".format(files), "green")
        for file in files:
            if file.endswith('.py'):
                extras.append(file)
    print("[ + ] Persistance Modules: [ + ]")
    for files in os.listdir('./data/scripts/persistance/'):
        cprint("[ + ] {} [ + ]".format(files), "green")
        for file in files:
            if file.endswith(".py"):
                persist.append(file)
    try:
        for entry in extras[0:]:
            print("[ + ] Your choices are: \n -> {}".format(entry))
        choice = int(input("Please enter your choice:\n->"))
        if choice != '':
            print(extras[choice])
    except (ValueError, IndexError, TypeError) as e:
        cprint("[ !! ] Incorrect Choice.. Try again. [ !! ]\n {}".format(e), "red")
        pass

if __name__ == "__main__":
    while True:
        extras_scan()
