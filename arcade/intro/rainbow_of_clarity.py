# Determine if the given character is a digit or not.

# Example

# For symbol = '0', the output should be
# isDigit(symbol) = true;
# For symbol = '-', the output should be
# isDigit(symbol) = false.
def isDigit(symbol):
    return symbol.isdigit()

# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.
# Example

# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc".

def lineEncoding(s):
    result_s = ''
    i = 0
    while i < len(s):
        s_count = 1
        while i < len(s) - 1   and s[i] == s[i+1]:
            s_count += 1
            i += 1
        if i < len(s) - 1:
            if s_count != 1:
                result_s += str(s_count) + s[i]
            else:
                result_s += s[i]
        elif i == len(s) - 1 and s_count > 1:
             result_s += str(s_count) + s[-1]
        else:
            result_s += s[i]
        
        i += 1   
    return result_s

# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

def chessKnight(cell):
    #
    column_name = 'ABCDEFGH'
    columns = dict()
    for i in range(len(column_name)):
        columns[column_name[i]] = columns.get(column_name[i],0) + i

    col, row  = columns[cell[0]] , int(cell[1]) - 1
    movements = list()
    # upper left
    movements.append([row - 2,col - 1])
    movements.append([row - 1,col - 2])
    #upper right
    movements.append([row - 2,col + 1])
    movements.append([row - 1,col + 2])

    # bottom left
    movements.append([row + 1,col - 2])
    movements.append([row + 2,col - 1])

    #bottom right
    movements.append([row + 1,col + 2])
    movements.append([row + 2,col + 1])
    counter = 0
    for movement in movements:
        if movement[0] >= 0 and movement[1] >=0 and movement[0] < 8 and movement[1] < 8:
            counter += 1
    return counter

# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

# For n = 152, the output should be
# deleteDigit(n) = 52;
# For n = 1001, the output should be
# deleteDigit(n) = 101.

def deleteDigit(n):
    #
    digits = str(n)
    i = 0
    biggest_number = 0
    while i < len(digits):
        # create new number deleting ith digit
        new_digit = int(digits[0:i] + digits[i+1:])
        if new_digit > biggest_number:
            biggest_number = new_digit
        i += 1
    return biggest_number

def main():
    print(deleteDigit(152))
    # print(chessKnight('A1'))
    # s = "aabbbc"
    # print(lineEncoding(s))

if __name__ == '__main__':
    main()