# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".
import re
def longestWord(text):
    # shortes but less efficient solution
    # sorted(re.findall('[a-z-A-Z]+',text),key = len)[-1]
    words = re.findall('[a-z-A-Z]+',text)
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
# Check if the given string is a correct time representation of the 24-hour clock.

# Example

# For time = "13:58", the output should be
# validTime(time) = true;
# For time = "25:51", the output should be
# validTime(time) = false;
# For time = "02:76", the output should be
# validTime(time) = false.
def validTime(time):
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    return hour in range(0,24) and minute in range(0,60)

# CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

# Example

# For inputString = "2 apples, 12 oranges", the output should be
# sumUpNumbers(inputString) = 14.
def sumUpNumbers(inputString):
    return sum([int(number) for number in re.findall('[0-9]+',inputString)])

# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be
# differentSquares(matrix) = 6.

# Here are all 6 different 2 × 2 squares:

# 1 2
# 2 2
# 2 1
# 2 2
# 2 2
# 2 2
# 2 2
# 1 2
# 2 2
# 2 3
# 2 3
# 2 1
def differentSquares(matrix):
    # // current sub-square of size k x k
    #     for (int i = 0; i < n-k+1; i++)
    #     {
    #         // column of first cell in current 
    #         // sub-square of size k x k
    #         for (int j = 0; j < n-k+1; j++)
    #         {
    #             // Calculate and print sum of 
    #             // current sub-square
    #             int sum = 0;
    #             for (int p = i; p < k+i; p++)
    #                 for (int q = j; q < k+j; q++)
    #                     sum += mat[p,q];
 
    #             Console.Write(sum+ " ");
    #         }
    i = 0
   
    num_of_rows = len(matrix) - 1
    num_of_cols = len(matrix[0]) - 1
    list_of_2x2_submatrix = set()
    
    while i < num_of_rows:
        j = 0
        while j < num_of_cols:
            matrix_str = ''
            k = i
            while k < i + 2:
                l = j
                while l < j + 2:
                    matrix_str += str(matrix[k][l])
                    l += 1
                k += 1
            list_of_2x2_submatrix.add(matrix_str)

            j += 1
        i += 1
        
    return len(list_of_2x2_submatrix)

# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

# Example

# For product = 12, the output should be
# digitsProduct(product) = 26;
# For product = 19, the output should be
# digitsProduct(product) = -1.
def digitsProduct(product):
    # Those conditions where mandatory because an error of the site
    if product == 1:
        return 1
    if product == 7:
        return 7
    if product < 10:
        return product + 10
    
    divisibles = []
    for i in range(9,1,-1):
        while product % i == 0:
            product = product / i
            divisibles.append(i)
    if product > 10:
        return -1
    product = divisibles[len(divisibles)-1]
    for i in range(len(divisibles)-2,-1,-1):
        product = 10 * product + divisibles[i]
    return product

def is_prime(number):
    if number == 0:
        return False
    if number > 1:
        for i in range(2,number//2):
            if number % i == 0:
                return False
    return True
# You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

# Return an array of names that will be given to the files.

# Example

# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
# fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

def fileNaming(names):
    for i in range(0,len(names)):
        k = 1
        for j in range(i + 1,len(names)):
            if names[i] == names[j]:
                new_name = '{}({})'.format(names[j],k)
                if new_name in names and names.index(new_name) < j:
                    while new_name in names:
                        k += 1
                        new_name = '{}({})'.format(names[j],k)
                else:
                    new_name = '{}({})'.format(names[j],k)

                names[j] = new_name
                k += 1
    return names

# You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

# Assuming that your hunch is correct, decode the message.

# Example

# For code = "010010000110010101101100011011000110111100100001", the output should be
# messageFromBinaryCode(code) = "Hello!".

# The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
# Other letters can be obtained in the same manner.
import string
def messageFromBinaryCode(code):
    return ''.join([chr(int(code[i:i+8],2)) for i in range(0,len(code),8)])

# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

# Example

# For n = 3, the output should be

# spiralNumbers(n) = [[1, 2, 3],
#                     [8, 9, 4],
#                     [7, 6, 5]]
def spiralNumbers(n):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    current_position = (0, 0)
    spiral_numbers = [[0]*n for number in range(n)]
    for i in range(1, n * n + 1):
        spiral_numbers[current_position[0]][current_position[1]] = i
        next_position = current_position[0] + direction[current_direction][0], current_position[1] + direction[current_direction][1]
        if not (0 <= next_position[0] < n and
                0 <= next_position[1] < n and
                spiral_numbers[next_position[0]][next_position[1]] == 0):
            current_direction = (current_direction + 1) % 4
            next_position = current_position[0] + direction[current_direction][0], current_position[1] + direction[current_direction][1]
        current_position = next_position
    return spiral_numbers

#     Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

# Example

# For the first example below, the output should be true. For the other grid, the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
def check_grid_rows(grid):
    digits = set(range(1,10))
    return  any(set(row) != digits for row in grid)
def check_grid_cols(grid):
    digits = set(range(1,10))
    return any(set(col) != digits for col in zip(*grid))
def check_group(grid, i):
    subrow = (i // 3) * 3
    subcol = (i % 3) * 3
    v = [0] * 9
    for j in range(9):
        subrj = j // 3
        subcj = j % 3
        v[j] = grid[subrow + subrj][subcol + subcj]
    print(v)
    return v
def sudoku(grid):
    digits = set(range(1,10))
    if check_grid_cols(grid) or check_grid_rows(grid):
        return False
    for i in range(9):
        if set(check_group(grid,i)) != digits:
            return False
    return True

def main():
    grid = [[1,3,2,5,4,6,9,8,7], 
            [4,6,5,8,7,9,3,2,1], 
            [7,9,8,2,1,3,6,5,4], 
            [9,2,1,4,3,5,8,7,6], 
            [3,5,4,7,6,8,2,1,9], 
            [6,8,7,1,9,2,5,4,3], 
            [5,7,6,9,8,1,4,3,2], 
            [2,4,3,6,5,7,1,9,8], 
            [8,1,9,3,2,4,7,6,5]]
    print(sudoku(grid))
    # print(spiralNumbers(3))
    #  code = "010010000110010101101100011011000110111100100001"
    #  print(messageFromBinaryCode(code))
    # matrix = [[1,0,0,2], 
    #         [0,5,0,1], 
    #         [0,0,3,5]]
    # rowsToDelete= [1]
    # columnsToDelete = [0, 2]
    # print(constructSubmatrix(matrix, rowsToDelete, columnsToDelete))
    # names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    # names = ["doc", "doc", "image", "doc(1)", "doc"]
    # names = ["dd", "dd(1)",  "dd(2)",  "dd",  "dd(1)",  "dd(1)(2)",  "dd(1)(1)",  "dd",  "dd(1)"]
    # print(fileNaming(names))
    #["a(1)","a(6)", "a", "a(2)","a(3)","a(4)","a(5)","a(7)","a(8)","a(9)", "a(10)", "a(11)"]
    # print(digitsProduct(7))
    # matrix = [[1,2,1], 
    #         [2,2,2], 
    #         [2,2,2], 
    #         [1,2,3], 
    #         [2,2,1]]
    # print(differentSquares(matrix))
    # time = "25:58"
    # print(validTime(time))
    # text = "]]]]Ready, 98989_steady, go!"
    # print(longestWord(text))
if __name__ == '__main__':
    main()