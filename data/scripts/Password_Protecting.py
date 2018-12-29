import hashlib
import sys

password = ""

def main():
    # Code goes here
    print "We Are Working :)"
    sys.exit(0)


while True:
    input = raw_input("Enter Password Please: ")
    if hashlib.md5(input).hexdigest() == password:
        print "Welcome to the program"
        main()
    else:
        print "Doesnt Seem Right... Try again!"