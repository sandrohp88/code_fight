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
    while i < len(inputArray) -1 :
        temp_product = inputArray[i]*inputArray[i+1]
        if temp_product > greater_consecutive_product:
            greater_consecutive_product = temp_product
        i+=1
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
    while i <  n:
        new_value =  array_result[-1] + 2 * (i + 1) + 2*(i-1)
        array_result.append(new_value)
        i+=1
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
    while i < len(statues) -1:
        counter += sorted_statues[i+1] - sorted_statues[i] -1
        i+=1
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

# TODO Unfinished!!!
def almostIncreasingSequence(sequence):
    sequence_lenght = len(sequence)
    if sequence_lenght == 2:
        return True
    if isSorted(sequence[1:]):
        return True
    if isSorted(sequence[:-1]):
        return True
        
    i = 1
    counter = 0
    while i <= sequence_lenght - 2 and counter < 2:
        if sequence[i] >= sequence[i+1] or sequence[i] <= sequence[i - 1]:
            new_sequence = []
            new_sequence.extend(sequence[:i])
            new_sequence.extend(sequence[i+1:])
            if isSorted(new_sequence):               
                    sequence.pop(i)
                    sequence_lenght = len(sequence)
                    i -= 1        
                    counter += 1
            else:
                counter += 2
            
        i+=1
    return counter < 2

def isSorted(sequence):
    previous = sequence[0]
    a = sequence[1:]
    for current in a:
        if previous >= current:
            return False
        previous = current
    return True
def main():
    pass

if __name__ == '__main__':
    main()