
import numpy as np
# Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong 
# (the strongest arm can be both the right and the left), and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

# Example

# For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 9, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
      return (((yourLeft + yourRight) == (friendsLeft+friendsRight))) and (max(yourLeft,yourRight) == max(friendsLeft,friendsRight))

# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(inputArray):
    max_absolute_difference = 0
    for i in range(1, len(inputArray) -1 ,2):
        new_difference = max(abs(inputArray[i] - inputArray[i - 1]),abs(inputArray[i] - inputArray[i + 1]))
        if new_difference > max_absolute_difference:
            max_absolute_difference = new_difference
    return max_absolute_difference

# An IP address is a numerical label assigned to each device 
# (e.g., computer, printer) participating in a computer network 
# that uses the Internet Protocol for communication. There are 
# two versions of the Internet protocol, and thus two versions of addresses. 
# One of them is the IPv4 address.

# IPv4 addresses are represented in dot-decimal notation, 
# which consists of four decimal numbers, each ranging 
# from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example

# For inputString = "172.16.254.1", the output should be
# isIPv4Address(inputString) = true;

# For inputString = "172.316.254.1", the output should be
# isIPv4Address(inputString) = false.

# 316 is not in range [0, 255].

# For inputString = ".254.255.0", the output should be
# isIPv4Address(inputString) = false.

# There is no first number.

def isIPv4Address(inputString):        
     #
     
     
     ip_address = inputString.split('.')
     for ip in ip_address:
         if ip == '' or not ip.isnumeric():
             return False
         if int(ip) < 0 or int(ip) > 255:
            return False
     return True

# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. 
# You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.

# Check out the image below for better understanding:
def avoidObstacles(inputArray):
    #  
    max_number = max(inputArray)
    obstacules_list = [False] *  (max_number + 2 )
    for i in inputArray:
        obstacules_list[i] = True
    minimal_length = 2
    
    reach_final = False
    while not reach_final:
        i = minimal_length
        while i < len(obstacules_list) and not obstacules_list[i] :
            i += minimal_length
            
        if i >= len(obstacules_list):
            # I reach the end, so I found the minimal_length
            reach_final = True
        else:
            minimal_length += 1
    return minimal_length

# Last night you partied a little too hard. 
# Now there's a black and white photo of you 
# that's about to go viral! You can't let this 
# ruin your reputation, so you want to apply the 
# box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers. 
# The algorithm distorts the input image in the following way: 
# Every pixel x in the output image has a value equal to the 
# average value of the pixel values from the 3 × 3 square 
# that has its center at x, including x itself. 
# All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

# Example

# For

# image = [[1, 1, 1], 
#          [1, 7, 1], 
#          [1, 1, 1]]
# the output should be boxBlur(image) = [[1]].

# To get the value of the middle pixel in the input 3 × 3 square: 
# (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
# The border pixels are cropped from the final result.

# For

# image = [[7, 4, 0, 1], 
#          [5, 6, 2, 2], 
#          [6, 10, 7, 8], 
#          [1, 4, 2, 0]]
# the output should be

# boxBlur(image) = [[5, 4], 
#                   [4, 4]]
# There are four 3 × 3 squares in the input image, so there 
# should be four integers in the blurred output. 
# To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. 
# The other three integers are obtained the same way, 
# then the surrounding integers are cropped from the final result.
def boxBlur(image):
    #
    row_num = len(image)
    column_num = len(image[0])
    squares_horizontal = row_num - 2
    squares_vertical = column_num - 2
   
    
    row = 0
    col = 0
    result = list()
    one_row = list()
    np_image = np.array(image)
    while row < squares_horizontal:
        while col < squares_vertical:
            blur_number = sum( sum(np_image[row :row + 3,col: col +3])) // 9
            one_row.append(blur_number)
            col +=1
        result.append(one_row.copy())
        one_row.clear()
        row += 1
        col = 0
    return result

# In the popular Minesweeper game you have a board with some 
# mines and those cells that don't contain a mine have a number
# in it that indicates the total number of mines in the neighboring cells. 
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be

# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]       
def minesweeper(matrix):
# Iterate through the matrix and every time I find True
# add 1 to the neighbors

    
    mine_sweeper = list()
    for i in range(len(matrix)):
        mine_sweeper.append([0] * len(matrix[i]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If find True add one to all neighbors
            if matrix[i][j] == True:
                #Left upper corner
                if i == 0 and j == 0:
                    mine_sweeper[ i ][ j + 1 ] +=1 # Right
                    mine_sweeper[ i + 1 ][ j + 1 ] +=1 # Diag
                    mine_sweeper[ i + 1 ] [ j ] +=1 # Bottom
                # Left bottom corner
                elif i == len(matrix) - 1 and j == 0:
                    mine_sweeper[ i - 1 ][ j ] +=1 # Up
                    mine_sweeper[ i  ][ j + 1 ] +=1 # Right
                    mine_sweeper[ i - 1 ] [ j  +  1] +=1
                # Right upper corner
                elif i == 0 and j == len(matrix[i]) - 1:
                    mine_sweeper[ i ][ j - 1 ] +=1 # Left
                    mine_sweeper[ i + 1 ][ j - 1 ] +=1 # Diag
                    mine_sweeper[ i + 1 ] [ j ] +=1 # Bottom
                # Rigth bottom corner
                elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                    mine_sweeper[ i - 1 ][ j ] +=1 # Up
                    mine_sweeper[ i ][ j - 1 ] +=1 # Left
                    mine_sweeper[ i - 1 ] [ j - 1 ] +=1 # Diag
                # Left border
                elif j == 0 and i > 0 and i < len(matrix) - 1:
                    mine_sweeper[ i - 1 ][ j ] +=1 # Up
                    mine_sweeper[ i + 1 ][ j ] +=1 # Down
                    mine_sweeper[ i ] [ j + 1 ] +=1 # Rigth
                    # Diagonls
                    mine_sweeper[ i - 1 ][ j + 1] +=1
                    mine_sweeper[ i + 1 ][ j + 1 ] +=1
                    # mine_sweeper[ i ] [ j + 1 ] +=1
                # Rigth border
                elif j == len(matrix[i]) - 1 and i < len(matrix) - 1 and i > 0:
                    mine_sweeper[ i - 1 ][ j ] +=1 # Up
                    mine_sweeper[ i + 1 ][ j ] +=1 # Down
                    mine_sweeper[ i ] [ j - 1 ] +=1 # Left
                    # Diagonls
                    mine_sweeper[ i - 1 ][ j - 1] +=1
                    mine_sweeper[ i + 1 ][ j - 1 ] +=1
                # Upper border
                elif i == 0 and j > 0  and j < len(matrix[i]) - 1 :
                    mine_sweeper[ i ][ j + 1 ] += 1 # Right
                    mine_sweeper[ i + 1 ][ j ] += 1 # Down
                    mine_sweeper[ i ] [ j - 1 ] += 1 # Left
                    # Diagonls
                    mine_sweeper[ i + 1 ][ j - 1] +=1
                    mine_sweeper[ i + 1 ][ j + 1 ] +=1
                # Bottom border
                elif i == len(matrix) - 1 and j < len(matrix[i]) - 1 and j > 0:
                    mine_sweeper[ i ][ j + 1 ] += 1 # Right
                    mine_sweeper[ i - 1 ][ j ] += 1 # Up
                    mine_sweeper[ i ] [ j - 1 ] += 1 # Left
                    # Diagonls
                    mine_sweeper[ i - 1 ][ j - 1] +=1
                    mine_sweeper[ i - 1][ j + 1 ] +=1
                # Have 9 neighbours
                elif i > 0 and i < len(matrix) - 1 and j > 0 and j < len(matrix[i]) - 1:
                    mine_sweeper[ i ][ j + 1 ] += 1 # Right
                    mine_sweeper[ i - 1 ][ j ] += 1 # Up
                    mine_sweeper[ i + 1 ] [ j ] += 1 # Down
                    mine_sweeper[ i ] [ j - 1 ] += 1 # Left
                    # Diagonls
                    mine_sweeper[ i - 1 ][ j - 1] +=1
                    mine_sweeper[ i - 1 ][ j + 1] +=1
                    mine_sweeper[ i + 1 ][ j + 1 ] +=1
                    mine_sweeper[ i + 1 ][ j - 1 ] +=1

                
    return mine_sweeper

                
          
   
   
    


def main():
    matrix = [[True, False, False],
           [False, True, False],
           [False, False, False]]

    matrix2 = [[True,False,False,True], 
    [False,False,True,False], 
    [True,True,False,True]]
    
    print(minesweeper(matrix2))
    # image1 = [[7, 4, 0, 1], 
    #          [5, 6, 2, 2], 
    #          [6, 10, 7, 8], 
    #          [1, 4, 2, 0]]
   
   
    # image = [[1, 1, 1], 
    #         [1, 7, 1], 
    #         [1, 1, 1]]

    # image2 = [[36,0,18,9], 
    #         [27,54,9,0], 
    #          [81,63,72,45]]
    # image3 = [[36,0,18,9,9,45,27], 
    #         [27,0,54,9,0,63,90], 
    #         [81,63,72,45,18,27,0], 
    #         [0,0,9,81,27,18,45], 
    #         [45,45,27,27,90,81,72], 
    #         [45,18,9,0,9,18,45], 
    #         [27,81,36,63,63,72,81]]

    # image4 = [[1,2,3,4,5,6,7,8,9],
    #         [1,2,3,4,5,6,7,8,9],
    #         [1,2,3,4,5,6,7,8,9]]
    # print(boxBlur(image4))

#     [[39,30,26,25,31], 
#    [34,37,35,32,32], 
#   [38,41,44,46,42], 
#   [22,24,31,39,45], 
#   [37,34,36,47,59]]


    # yourLeft = 10
    # yourRight = 15
    # friendsLeft = 15
    # friendsRight = 10
    # print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))
    # inputArray = [2, 4, 1, 0]
    # print(arrayMaximalAdjacentDifference(inputArray))
    # inputString = "172.316.254.1"
    # print(isIPv4Address(inputString))
    # inputArray = [19, 32, 11, 23]
    
    # print(avoidObstacles(inputArray))


if __name__ == '__main__':
    main()


#     [[0,2,2,1], 
#  [3,4,3,3], 
#  [1,2,3,1]]