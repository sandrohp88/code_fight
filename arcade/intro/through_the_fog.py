# Consider integer numbers from 0 to n - 1 written down along the 
# circle in such a way that the distance between any two neighbouring 
# numbers is equal (note that 0 and n - 1 are neighbouring, too).

# Given n and firstNumber, find the number which is written in the 
# radially opposite position to firstNumber.

# Example

# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.
def circleOfNumbers(n, firstNumber):
    #
    middle = n//2
    if firstNumber > middle:
        return firstNumber - middle
    elif firstNumber == middle:
        return 0
    elif firstNumber == 0:
        return middle

    else:
        return (firstNumber + middle)

# You have deposited a specific amount of dollars into your bank account. 
# Each year your balance increases at the same growth rate. 
# Find out how long it would take for your balance to pass a 
# specific threshold with the assumption that you don't make any additional deposits.

# Example

# For deposit = 100, rate = 20 and threshold = 170, the output should be
# depositProfit(deposit, rate, threshold) = 3.

# Each year the amount of money on your account increases by 20%. 
# It means that throughout the years your balance would be:

# year 0: 100;
# year 1: 120;
# year 2: 144;
# year 3: 172,8.
# Thus, it will take 3 years for your balance to pass the threshold, which is the answer.
def depositProfit(deposit, rate, threshold):
    #
    number_of_years = 0
    while deposit < threshold:
        deposit += rate*deposit/100 
        number_of_years += 1
    return number_of_years 

# Given a sorted array of integers a, find an integer x from a such that the value of
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
# is the smallest possible (here abs denotes the absolute value).
# If there are several possible answers, output the smallest one.

# Example

# For a = [2, 4, 7], the output should be
# absoluteValuesSumMinimization(a) = 4.
def absoluteValuesSumMinimization(a):
   #
   small = 99999999999999999999
   for i in range(len(a)):
       numbers_sum = 0
       j = 0
       while j < len(a):
           numbers_sum += abs(a[j] - a[i])
           j += 1
        
       if numbers_sum < small:
                small = numbers_sum
                index = i
   return a[index]

# Given an array of equal-length strings, check if it is 
# possible to rearrange the strings in such a way that after 
# the rearrangement the strings at consecutive positions 
# would differ by exactly one character.

# Example

# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false;

# All rearrangements don't satisfy the description condition.

# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.

# Strings can be rearranged in the following way: "aa", "ab", "bb".
# TODO
from itertools import permutations
def stringsRearrangement(inputArray):
    #
    for permutation in permutations(inputArray,len(inputArray)):
        if ordered_almost_equal(permutation):
            return True
    return False

def  ordered_almost_equal(input_array):
    i = 0
    while i < len(input_array) - 1:
        if not almost_equal(input_array[i],input_array[i + 1]):
            return False
        i += 1
    return True
def almost_equal(string1, string2):
    pass
    different_character_count = 0
    index = 0
    while index < len(string1) and different_character_count < 2:
        if string1[index] != string2[index]:
            different_character_count += 1

        index += 1
    return different_character_count == 1



def main():
    # n = 10 
    # firstNumber = 2
    # print(circleOfNumbers(n,firstNumber))
    # deposit = 100 
    # rate = 20 
    # threshold = 170
    # print(depositProfit(deposit, rate, threshold))
    # a = [2, 4, 7]
    # print(absoluteValuesSumMinimization(a))
    # string1, string2 = 'abce','bbcd'
    # print(almost_equal(string1, string2))
    inputArray = ["ab", "bb", "aa"]
    print(stringsRearrangement(inputArray))


if __name__ == '__main__':
    main()