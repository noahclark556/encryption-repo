from random import seed
from random import randint
import time
import parseUpload
from pip._vendor.distlib.compat import raw_input
from os import system, name

firstSeed = 0
newString = ""
key2 = 7
realDe = 0
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "~", "@",
            "#", "$", "%", "^", "&", "*", "(", ")", "?", ">", "<", "|", "[", "]", "{", "}", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "0", "/", "A",
            "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z", "_", " "]


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def make(seed):
    cycle = int(seed)
    x = int(seed)
    global key2
    counter = 0
    size = len(alphabet)
    while (x > size - 1):

        cycle -= size
        x -= size
        out = size + cycle * 2
        out2 = cycle * 3
        value = randint(0, size-3) #random index to display on screen to represent progress while sequence is running
        value2 = randint(0, size-1) #random index to display on screen to represent progress while sequence is running
        value3 = randint(0, 300) #random index to display on screen to represent progress while sequence is running
        value4 = randint(0, size -1) #random index to display on screen to represent progress while sequence is running
        print("Creating Crypto.. " + str(x) + " ---- " + str(out2) + " ---- " + str(out) + " ---- KEY: " + alphabet[value] + " ---- " + alphabet[value2] + " ---- " + str(value3) + " ---- " + alphabet[value4] + " ------ Not Ready")
        print("Progress: " + str(len(newString) + 1) + "/" + str(len(alphabet)))
        counter+=1
        # if(counter == 500):
        #     print("Available Key Found")
        #     counter = 0
        #     time.sleep(.04) give user time to see that a key has been found


    global firstSeed
    firstSeed = cycle + key2
    key2 += size
    return (cycle)

    # if newString.find(alphabet[cycle]) == -1:
    #
    #     newString += alphabet[cycle]
    #     key2 -= 1
    #     cycle=newseed+key2
    #     print(mainCycle)
    #     x+=1
    # else:
    #     key2 -= 1
    #     cycle = newseed + key2


def begin():
    global firstSeed
    global newString
    global key2
    global realDe
    size = len(alphabet)
    firstSeed = 0
    newString = ""
    key2 = 7
    realDe = 0
    print("Enter a unique, NUMBER ONLY, seed. (The bigger, the more powerful):")
    print("Example (Do not use): 277639274")
    seed = raw_input()
    print("Enter a DE key (double encryption, recommended to be between 20 and 300, higher numbers can cause\n "
          "process to be exponentially longer): ")
    print("Example (Do not use): 230")
    DE = raw_input()
    realDe = DE
    key2 = int(DE)
    print("DO NOT forget your seed AND DE, that is your only means of decryption if a new crypto is uploaded")
    print("Your seed will now create a table, the table will be uploaded to a database and used as the current "
          "encryption method")


    firstSeed = seed
    x = 0
    while (x < size):
        letter = make(firstSeed)

        if (letter > -1):
            # print(str(x) + alphabet[letter])
            if newString.find(alphabet[letter]) == -1:
                newString += alphabet[letter]

                print("Found valid key " + alphabet[letter])
                time.sleep(.06)

                # if(x == size-1):
                #     print('"' + alphabet[x] + '":"' + alphabet[letter] + '"\n')
                # else:
                #     print('"' + alphabet[x] + '":"' + alphabet[letter] + '",\n')
                x += 1
        # if(len(newString) == len(alphabet)): #THIS IS BETAAAAA, IF PROBLEMS FORM, REMOVE THIS CODE AND ALL LETTER after " " IN ALPHABET
        #     x = size
        #     x+=1;
        # else:
        #     return
    parseUpload.upload(newString)
    print("Parsing...")
    time.sleep(4)

    clear()
    print("KEY INFO : \n\n")
    print("Uploaded to database successfully:\nCurrently being used as active crypto\nDO NOT change crypto if you do "
          "not remember your seed or DE \nSeed: " + str(seed) + "\nDE Key: " + str(realDe) + "\n\n")
