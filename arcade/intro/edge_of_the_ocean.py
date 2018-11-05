# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer inputArray

# An array of integers containing at least two elements.

# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.

# [output] integer

# The largest product of adjacent elements.


def adjacentElementsProduct(inputArray):
    greater_consecutive_product = inputArray[0]*inputArray[1]
    i = 1
    while i < len(inputArray) - 1:
        temp_product = inputArray[i]*inputArray[i+1]
        if temp_product > greater_consecutive_product:
            greater_consecutive_product = temp_product
        i += 1
    return greater_consecutive_product

# Below we will define an n-interesting polygon.
# Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1.
# An n-interesting polygon is obtained by taking the n - 1-interesting
# polygon and appending 1-interesting polygons to its rim, side by side.
# You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

# Example

# For n = 2, the output should be
# shapeArea(n) = 5;
# For n = 3, the output should be
# shapeArea(n) = 13.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n < 104.

# [output] integer

# The area of the n-interesting polygon.


def shapeArea(n):

    if n == 1:
        return 1
    array_result = []
    array_result.append(1)
    array_result.append(5)
    i = 2
    while i < n:
        new_value = array_result[-1] + 2 * (i + 1) + 2*(i-1)
        array_result.append(new_value)
        i += 1
    return array_result[-1]

# Ratiorg got statues of different sizes as a present from CodeMaster
# for his birthday, each statue having an non-negative integer size.
# Since he likes to make things perfect, he wants to arrange them from
# smallest to largest so that each statue will be bigger than the previous
# one exactly by 1. He may need some additional statues to be able to accomplish that.
# Help him figure out the minimum number of additional statues needed.

# Example

# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.

# Ratiorg needs statues of sizes 4, 5 and 7.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer statues

# An array of distinct non-negative integers.

# Guaranteed constraints:
# 1 ≤ statues.length ≤ 10,
# 0 ≤ statues[i] ≤ 20.

# [output] integer

# The minimal number of statues that need to be added to existing
# statues such that it contains every integer size from an
# interval [L, R] (for some L, R) and no other sizes.


def makeArrayConsecutive2(statues):
    sorted_statues = sorted(statues)
    counter = 0
    i = 0
    while i < len(statues) - 1:
        counter += sorted_statues[i+1] - sorted_statues[i] - 1
        i += 1
    return counter

# Given a sequence of integers as an array, determine whether
# it is possible to obtain a strictly increasing sequence by removing
# no more than one element from the array.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false;

# There is no one element in this array that can be removed
# in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.

# You can remove 3 from the array to get the strictly
# increasing sequence [1, 2]. Alternately, you can
# remove 2 to get the strictly increasing sequence [1, 3].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer sequence

# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -105 ≤ sequence[i] ≤ 105.

# [output] boolean

# Return true if it is possible to remove one element
# from the array in order to get a strictly increasing sequence,
# otherwise return false.


def almostIncreasingSequence(sequence):
    if len(sequence) < 3:
        return True
    if isSorted(sequence[1:]):
        return True
    if isSorted(sequence[:-1]):
        return True

    indexes = []
    i = 1
    current_element = sequence[i]
    while i < len(sequence) - 1:
        if current_element >= sequence[i + 1] or current_element <= sequence[i - 1]:
            indexes.append(i)
            #current_element = sequence[i + 1]
        i += 1
        current_element = sequence[i]
    if len(indexes) > 2:
        return False
    if len(indexes) == 2:
        # Check if removing one of the elements the sequence is ordered
        new_sequence = sequence[:indexes[0]] + sequence[indexes[0] + 1:]
        if isSorted(new_sequence):
            return True
        else:
            new_sequence = sequence[:indexes[1]] + sequence[indexes[1] + 1:]
            return isSorted(new_sequence)

    else:
        return len(indexes) == 1 and isSorted(sequence[:indexes[0]] + sequence[indexes[0] + 1:])


def isSorted(sequence):
    previous = sequence[0]
    a = sequence[1:]
    for current in a:
        if previous >= current:
            return False
        previous = current
    return True

# After they became famous, the CodeBots all decided to move to a new
# building and live together. The building is represented by a
# rectangular matrix of rooms. Each cell in the matrix contains
# an integer that represents the price of the room. Some rooms
# are free (their cost is 0), but that's probably because they
# are haunted, so all the bots are afraid of them. That is why
# any room that is free or is located anywhere below a free room
# in the same column is not considered suitable for the bots to live in.

# Help the bots calculate the total price of all the rooms that are suitable for them.

# Example

# For
# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
# the output should be
# matrixElementsSum(matrix) = 9.

# Here's the rooms matrix with unsuitable rooms marked with 'x':

# [[x, 1, 1, 2],
#  [x, 5, x, x],
#  [x, x, x, x]]
# Thus, the answer is 1 + 5 + 1 + 2 = 9.

# For
# matrix = [[1, 1, 1, 0],
#           [0, 5, 0, 1],
#           [2, 1, 3, 10]]
# the output should be
# matrixElementsSum(matrix) = 9.

# Here's the rooms matrix with unsuitable rooms marked with 'x':

# [[1, 1, 1, x],
#  [x, 5, x, x],
#  [x, 1, x, x]]
# Note that the free room in the first row make the full column unsuitable for bots.

# Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
#


def matrixElementsSum(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    price = 0
    for i in range(number_of_columns):
        j = 0
        while j < number_of_rows and matrix[j][i] != 0:
            price += matrix[j][i]
            j += 1
    return price


def main():
    s = [1, 2, 1, 2]
    a = [1]
    matrix = [[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]]

    print(matrixElementsSum(matrix))

    # print(isSorted(a))
    # print(almostIncreasingSequence(a))
if __name__ == '__main__':
    main()
