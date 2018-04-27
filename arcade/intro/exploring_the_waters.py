# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    # find longest string
    max_len = 0
    for s in inputArray:
        if max_len < len(s):
            max_len = len(s)

    # contruct the list of the largest strings
    list_longest_string = []
    for s in inputArray:
        if len(s) == max_len:
            list_longest_string.append(s)
    return list_longest_string

# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def commonCharacterCount(s1, s2):
    number_common_characters = 0
    # Iterate over s1 one character at the time
    # look for that character in s2.
    # If found increment number_common_characters.
    # Delete that character from s2 and move to the next 
    # character in s1

    for s1_character in s1:
        found_index = s2.find(s1_character)
        if found_index != -1:
            number_common_characters += 1
            s2 = s2[:found_index] + s2[found_index + 1 :] 
    return number_common_characters

# Ticket numbers usually consist of an even number of digits. 
# A ticket number is considered lucky if the sum of the first 
# half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    #
    n_string = str(n)
    number_of_digits = len(n_string)
    # If number of digits is even
    if number_of_digits % 2 == 0:
        # Separate the two halves
        first_half = n_string[:number_of_digits // 2]
        second_half = n_string[(number_of_digits + 1) // 2 :]
        # Calculate the first_half sum
        first_half_sum = 0
        for digit in first_half:
            first_half_sum += int(digit)
         # Calculate the second_half sum
        second_half_sum = 0
        for digit in second_half:
            second_half_sum += int(digit)
        
        return first_half_sum == second_half_sum
    else:
        return False

# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their 
# heights in a non-descending order without moving the trees.

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer a

# If a[i] = -1, then the ith position is occupied by a tree. 
# Otherwise a[i] is the height of a person standing in the ith position.

# Guaranteed constraints:
# 5 ≤ a.length ≤ 15,
# -1 ≤ a[i] ≤ 200.
    
def sortByHeight(a):
    # Find all -1 position.
   
    minus_one_indexs = []
    len_a = len(a)
    for index in range(len_a):
        if a[index] == -1:
            minus_one_indexs.append(index)
    # Sort the list
    sorted_list = sorted(a)  
    # Remove all -1's
    sorted_list = sorted_list[len(minus_one_indexs):]  
    # print(sorted_list)
    for index in minus_one_indexs:
        sorted_list.insert(index,-1)
        # print(sorted_list)
        # print(sorted_list)

        # print()
    return sorted_list

# You have a string s that consists of English letters, 
# punctuation marks, whitespace characters, and brackets. 
# It is guaranteed that the parentheses in s form a regular bracket sequence.

# Your task is to reverse the strings contained in each 
# pair of matching parentheses, starting from the innermost pair. 
# The results string should not contain any parentheses.

# Example

# For string s = "a(bc)de", the output should be
# reverseParentheses(s) = "acbde".

def reverseParentheses(s):
    left_bracket_index = s.rfind('(')    
    right_bracket_index = left_bracket_index
    while  right_bracket_index < len(s) and s[right_bracket_index] != ')':
        right_bracket_index += 1
    while(left_bracket_index != -1):
        substring_to_replace = s[left_bracket_index:right_bracket_index + 1]
        reversed_substring = substring_to_replace[1:-1]
        reversed_substring = reversed_substring[::-1]
        s  = s.replace(substring_to_replace,reversed_substring, 1)
        left_bracket_index = s.rfind('(')    
        right_bracket_index = left_bracket_index
        while right_bracket_index < len(s) and s[right_bracket_index] != ')':
            right_bracket_index += 1
    return s



       

def main():
    # inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    # print(allLongestStrings(inputArray))

    # s1 = "aabcc" 
    # s2 = "adcaa"
    # print(commonCharacterCount(s1,s2))
    # a = [-1, 150, 190, 170, -1, -1, 160, 180]
    # print(sortByHeight(a))
    s = "a(bc)de"
    print(reverseParentheses(s))

if __name__ == '__main__':
    main()