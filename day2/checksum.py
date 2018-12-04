import sys

def checksum(data):
    twos = 0
    threes = 0
    for string in data:
        string = ''.join(sorted(string))
        for x in range(0, len(string)):
            tmp = 0
            for y in range(x + 1, len(string)):
                if string[x] == string[y]:
                    tmp += 1

            if tmp == 2:
                twos += 1
            elif tmp == 3:
                threes += 1

    return twos * threes

if __name__ == "__main__":
    print(checksum(sys.stdin))
