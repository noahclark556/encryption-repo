def main(newString, alphabet):
    size = len(alphabet)

    stringList = []
    stringList[:0] = newString

    parsedString = ""
    x = 0
    while(x < size):
        if(x == size - 1):
            parsedString += '"' + alphabet[x] + '":"' + newString[x] + '"'
        else:
            parsedString += '"' + alphabet[x] + '":"' + newString[x] + '",_'
        x+=1
    return parsedString
