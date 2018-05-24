import re
import string
import numpy as np

# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

# Example

# For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
# arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

def arrayReplace(inputArray, elemToReplace, substitutionElem):

    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray

# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
# For n = 642386, the output should be
# evenDigitsOnly(n) = false.

def evenDigitsOnly(n):
    str_number = str(n)

    for digit in str_number:
        if int(digit) % 2 != 0:
            return False
    return True


# Correct variable names consist only of English letters, 
# digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

# For name = &quot;var_1__Int&quot;, the output should be
# variableName(name) = true;
# For name = &quot;qq-q&quot;, the output should be
# variableName(name) = false;
# For name = &quot;2w2&quot;, the output should be
# variableName(name) = false.
def variableName(name):
    variable_name_re = '^[a-zA-Z_][a-zA-Z_0-9]*'
    result = re.match(variable_name_re,name)
    # return name.isIdentifier(); Cool!
    if result == None:
        return False
    return result.group() == name


# Given a string, replace each its character by the next 
# one in the English alphabet (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be
# alphabeticShift(inputString) = "dsbaz".

def alphabeticShift(inputString):
    #
    alphabet = list(string.ascii_lowercase)
    result = ''
    for character in inputString:
        if character == 'z':
            result += 'a'
        else:
            subs = alphabet[alphabet.index(character) + 1]
            result += subs
    
    return result

# Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.
def chessBoardCellColor(cell1, cell2):
    #
    column_name = 'ABCDEFGH'
    columns = dict()
    for i in range(len(column_name)):
        columns[column_name[i]] = columns.get(column_name[i],0) + i

    col1, row1  = columns[cell1[0]] , int(cell1[1]) - 1
    col2, row2 = columns[cell2[0]] , int(cell2[1]) - 1
    chess_board = [[1]*8 for x in range(8)]

    for row in range(0,8):        
        if row % 2 == 0:
            column = 0
        else:
            column = 1
        while column < 8:
            chess_board[row][column] = 0
            column += 2
    print(chess_board)
    return chess_board[row1][col1] == chess_board[row2][col2]


def is_even(number):
    return number%2 == 0
def main():
    # inputArray = [1, 2, 1]
    # print(arrayReplace(inputArray,1,3))
    # n = 642386
    # print(evenDigitsOnly(n))

    # name = 'sandrohp'
    # print(variableName(name))
    # inputString = "crazy"
    # print(alphabeticShift(inputString))
    cell1 = "C8" 
    cell2 = "H1"
    print(chessBoardCellColor(cell1,cell2))
if __name__ == '__main__':
    main()