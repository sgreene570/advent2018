import sys

def checksum(data):
    twoCount = 0
    threeCount = 0
    for string in data:
        string = ''.join(sorted(string))
        twoFound = False
        threeFound = False
        x = 0
        while x < len(string):
            char = string[x]
            tmp = string[x:string.rfind(char) + 1]
            size = len(tmp)
            if size == 2 and not twoFound:
                twoCount += 1
                twoFound = True
            elif size == 3 and not threeFound:
                threeCount += 1
                threeFound = True

            x += size

    return twoCount * threeCount

def commonLetters(data):
    strings = [x.strip() for x in data]
    strings.sort()
    size = len(strings)
    for x in range(0, size):
        for y in range(0, size):
            countDiffs = 0
            for a, b in zip(strings[x], strings[y]):
                if a!=b:
                    countDiffs += 1
            if countDiffs == 1:
                return strings[x], strings[y]

if __name__ == "__main__":
    #print(checksum(sys.stdin))
    print(commonLetters(sys.stdin))
