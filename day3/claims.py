import sys

def claims(commands):
    board = [][]
    for command in commands:
        codes = command.split(' ')
        idNum = codes[0][1:]
        coords = codes[2]
        left = coords[:coords.find(',')]
        right = coords[coords.find(',') + 1 : coords.find(':')]
        size = codes[3]
        width = size[:size.find('x')]
        height = size[size.find('x') + 1:]




if __name__ == "__main__":
    print(claims(sys.stdin))
