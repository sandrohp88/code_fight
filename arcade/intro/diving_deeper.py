
# Given array of integers, remove each kth element from it.

# Example

# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
def extractEachKth(inputArray, k):
  #
   elements_to_remove = list()
   for i in range(1,(len(inputArray)//k + 1),):
       elements_to_remove.append(inputArray[i*k -1])
   for element in elements_to_remove:
       inputArray.remove(element)
   return inputArray

# Find the leftmost digit that occurs in a given string.

# Example

# For inputString = "var_1__Int", the output should be
# firstDigit(inputString) = '1';
# For inputString = "q2q-q", the output should be
# firstDigit(inputString) = '2';
# For inputString = "0ss", the output should be
# firstDigit(inputString) = '0'.
import string
def firstDigit(inputString):
    #
    lef_most_digit = ''
    for s in inputString:
        if s in string.digits:
            lef_most_digit = s
            break 
    return lef_most_digit

# Given a string, find the number of different characters in it.

# Example

# For s = &quot;cabca&quot;, the output should be
# differentSymbolsNaive(s) = 3.

# There are 3 different characters a, b and c.  

def differentSymbolsNaive(s):
    return len({c for c in s})

# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.

def arrayMaxConsecutiveSum(inputArray, k):
   #
    max_sum = 0
    
    for i in range(k):
        max_sum += inputArray[i]
    next_sum = max_sum    
    for i in range(k-1,len(inputArray) - 1):
        next_sum = next_sum - inputArray[i+1 - k] + inputArray[i+1]
        if next_sum > max_sum:
            max_sum = next_sum
        
    return max_sum


def main():
    #  inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    #  k = 3
    #  print(extractEachKth(inputArray,k))
    #  inputString = "q2q-q"
    #  print(firstDigit(inputString))
    # s = 'cabca'
    # print(differentSymbolsNaive(s))
    inputArray = [2, 3, 5, 1, 6] 
    k = 2
    print(arrayMaxConsecutiveSum(inputArray,k))
if __name__ == '__main__':
    main()