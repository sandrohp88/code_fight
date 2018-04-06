# Write a function that returns the sum of two numbers.
# Example
# For param1 = 1 and param2 = 2, the output should be
# add(param1, param2) = 3.
def add(param1, param2):
    return param1 + param2

# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

# Example

# For year = 1905, the output should be
# centuryFromYear(year) = 20;
# For year = 1700, the output should be
# centuryFromYear(year) = 17.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer year

# A positive integer, designating the year.

# Guaranteed constraints:
# 1 ≤ year ≤ 2005.

# [output] integer

# The number of the century the year is in.
def centuryFromYear(year):
    if year%100 == 0:
        return year//100
    else:
        return year//100+1

# Given the string, check if it is a palindrome.

# Example

# For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A non-empty string consisting of lowercase characters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 105.

# [output] boolean

# true if inputString is a palindrome, false otherwise.
def checkPalindrome(inputString):

    word_lenght = len(inputString)
    if word_lenght%2 == 0: 
        firt_half_word = inputString[:word_lenght//2]
        last_half_word = inputString[word_lenght//2:]
    else:
        firt_half_word = inputString[:word_lenght//2]
        last_half_word = inputString[word_lenght//2 + 1:]   
    return firt_half_word == last_half_word[::-1]

def main():
    pass

if __name__ == '__main__':
    main()