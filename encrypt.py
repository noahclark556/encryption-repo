import tables
import make


def createEncrypt(listLength, newList):
    encryptedList = []
    loopx = 0
    keyList = tables.start()
    # find char in alphabet
    # match with char in keylist
    while loopx < listLength:
        char = newList[loopx]
        index = make.alphabet.index(char)
        newchar = keyList[index]
        encryptedList.append(newchar)
        loopx += 1
    parsedString = ''.join(encryptedList)
    # parsedString = parsedString.replace("_", " ")
    return (parsedString)


def createDecrypt(listLength, newList):
    encryptedList = []
    loopx = 0
    keyList = tables.start()
    # find char in alphabet
    # match with char in keylist
    while loopx < listLength:
        char = newList[loopx]
        index = keyList.index(char)
        newchar = make.alphabet[index]
        encryptedList.append(newchar)
        loopx += 1
    parsedString = ''.join(encryptedList)
    # parsedString = parsedString.replace("_", " ")
    return (parsedString)
