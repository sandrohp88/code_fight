
# Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.

# Example

# For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be
# growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

def growingPlant(upSpeed, downSpeed, desiredHeight):
    #
    counter = 0
    growing = 0
    while growing < desiredHeight:
        growing += upSpeed
        counter += 1
        if growing >= desiredHeight:
            break
        growing -= downSpeed
        
    return counter

# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

# Example

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

# You can only carry the first item.

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

# You're strong enough to take both of the items with you.

# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4 and maxW = 6, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

# You can't take both items, but you can take any of them.

def knapsackLight(value1, weight1, value2, weight2, maxW):
    #
    item1 = [value1,weight1]
    item2 = [value2, weight2]
    if (weight1 + weight2) <= maxW:
        return (value1 + value2)
    elif item1[1] <= maxW and item2[1] <= maxW:
        return max(item1[0],item2[0])
    elif item1[1] <= maxW:
        return item1[0]
    elif item2[1] <= maxW:
        return item2[0]
    else:
        return 0

# Given a string, output its longest prefix which contains only digits.

# Example

# For inputString="123aa1", the output should be
# longestDigitsPrefix(inputString) = "123"
import re
def longestDigitsPrefix(inputString):
    # re.findall('^\d*',inputString)[0] this work
    max_string = ''
    for d in inputString:
        if d.isdigit():
            max_string += d
    if len(max_string) < len(inputString):
        max_string = ''


    result = re.findall(r'(\d+)[a-zA-Z_]', inputString)
    
    for s in result:
        if len(s) > len(max_string):
            max_string = s
    return max_string

# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.

# Example

# For n = 5, the output should be
# digitDegree(n) = 0;
# For n = 100, the output should be
# digitDegree(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# digitDegree(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.

def digitDegree(n):
    #
    counter = 1
    if len(str(n)) == 1:
        return 0

    dig_sum = digits_sum(n)
    while dig_sum != 1 and len(str(dig_sum)) > 1:
        dig_sum = digits_sum(dig_sum)
        counter += 1

    return counter
    
#
def digits_sum(number):
    total_sum = 0
    for d in str(number):
        total_sum += int(d)
    return total_sum

# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


# Example

# For bishop = "a1" and pawn = "c3", the output should be
# bishopAndPawn(bishop, pawn) = true.



# For bishop = "h1" and pawn = "h3", the output should be
# bishopAndPawn(bishop, pawn) = false.
def bishopAndPawn(bishop, pawn):
    #
    column_name = 'abcdefgh'
    columns = dict()
    for i in range(len(column_name)):
        columns[column_name[i]] = columns.get(column_name[i],0) + i

    col1, row1  = columns[bishop[0]] , int(bishop[1]) - 1
    col2, row2 = columns[pawn[0]] , int(pawn[1]) - 1
    return (abs(row1 - row2) - abs(col1 - col2)) == 0

def main():
    # upSpeed = 100 
    # downSpeed = 10
    # desiredHeight = 910
    # print(growingPlant(upSpeed, downSpeed, desiredHeight))
    # value1 = 10
    # weight1 = 5
    # value2 = 6
    # weight2 = 4
    # maxW = 8
    # print(knapsackLight(value1, weight1, value2, weight2, maxW))
    # inputString="1231"    
    # print(longestDigitsPrefix(inputString))
    # print(digitDegree(99))
    bishop = "a1"
    pawn = "c3"
    print(bishopAndPawn(bishop, pawn))
if __name__ == '__main__':
    main()