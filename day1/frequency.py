import sys

def frequency(changes):
    i = 0
    seen = []
    changes = changes.readlines()
    x = 0
    size = len(changes)
    while 1:
        if x == size:
            x = 0
            continue
        change = changes[x]
        num = int(change[1:])
        if change[0] == "-":
            i -= num
        else:
            i += num

        if i in seen:
            return i
        else:
            seen.append(i)

        x += 1


if __name__ == "__main__":
    print(frequency(sys.stdin))
