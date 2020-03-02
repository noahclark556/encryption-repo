from pip._vendor.distlib.compat import raw_input
from os import system, name

import encrypt
import make
import tables


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def parseEncrypt(message):
    # message = message.replace(" ", "_")
    newList = []
    newList[:0] = message
    listLength = len(newList)
    print("\nEncrypted Message:\n" + encrypt.createEncrypt(listLength, newList) + "\n")


def main():
    print("Encryption service activated..")
    answer = raw_input("Would you like to create crypto, encrypt or decrypt? (c/e/d):")
    if answer == "c":
        make.begin()
    elif answer == "d":
        message = raw_input("Input encrypted message:")
        newList = []
        newList[:0] = message
        listLength = len(newList)
        print("Decrypted Message:\n\n" + encrypt.createDecrypt(listLength, newList) + "\n")
    elif answer == "e":
        message = raw_input("Input a message:")
        parseEncrypt(message)
    elif answer == "clear":
        clear()
    elif answer == "exit":
        exit()
    else:
        print("Incorrect Option")
    main()

clear()
main()
