import textwrap


def cycle(s):
    if len(set(s)) == 1:
        return 1
    if len(set(s)) == len(s):
        return len(s)
    current = ""
    counter = 0
    for i in range(len(s) - 1):
        current = s[i]
        for j in range(i+1, len(s)):
            cycle = current*3
            counter += 1
            if counter == len(s):
                return counter
            if s in cycle:
                return counter
            current = current + s[j]

    return counter


def beautifulText(inputString, l, r):
    white_spaces_index = [i+1 for i in range(
        len(inputString)) if inputString[i] == " "]
    print(white_spaces_index)
    for index in white_spaces_index:
        wrap = textwrap.wrap(inputString, index)
        if len(wrap[0]) == len(wrap[-1]) and len(wrap[0]) in range(l, r+1):
            return True
    return False


def runnersMeetings(startPosition, speed):
    meeting = 0
    met = 0 if len(startPosition) == len(set(startPosition)) else len(
        startPosition) - len(set(startPosition)) + 1
    if met > meeting:
        meeting = met
    startPosition = [s * 60 for s in startPosition]

    for _ in range(59940):
        for i in range(len(startPosition)):
            startPosition[i] += speed[i]
        met = 0 if len(startPosition) == len(set(startPosition)) else len(
            startPosition) - len(set(startPosition)) + 1
        if met > meeting:
            meeting = met

    return -1 if meeting == 0 else meeting


def christmasTree(levelNum, levelHeight):
    tree = list()
    # line  horizontal group of asterisks
    line = None

    # create the crown
    crown = ' '*(levelNum + levelHeight) + '*'
    tree.append(crown)
    tree.append(crown)
    crown = ' '*(levelNum + levelHeight - 1) + '***'
    tree.append(crown)
    first_line_asterisk = 5

    for ln in range(levelNum):
        num = levelNum - ln
        num_asterisk = first_line_asterisk
        # level collection of levelHeight lines stacked one on top of the other.
        level = list()
        line = ""
        for i in range(levelHeight):
            line = ' '*(num + levelHeight - i - 2) + (num_asterisk) * "*"
            num_asterisk += 2
            level.append(line)
        tree += level
        first_line_asterisk += 2
    # foot
    foot = (levelHeight + 1) * \
        '*' if levelHeight % 2 == 0 else levelHeight*'*'
    foot = ((len(line) - len(foot))//2)*' ' + foot
    for i in range(levelNum):
        tree.append(foot)

    return tree


def main():
    levelNum = 4
    levelHeight = 8
    print(christmasTree(levelNum, levelHeight))
    # startPosition = [1, 1000]
    # speed = [23, 22]
    # print(runnersMeetings(startPosition, speed))
    # inputString = "dht skq dkg"
    # l = 4
    # r = 10
    # print(textwrap.wrap(inputString, 13,))
    # print(len(inputString))
    # print(beautifulText(inputString, l, r))
    # s = "cabca"
    # print(cycle(s))


if __name__ == '__main__':
    main()
