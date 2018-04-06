
# Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

# Example

# For a = [2, 3, 3, 1, 5, 2], the output should be
# firstDuplicate(a) = 3.

# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

# For a = [2, 4, 3, 5, 1], the output should be
# firstDuplicate(a) = -1.

def firstDuplicate(a):
    dict_a = {}
    result = -1
    first_time = True
    for i in a:
        if i in dict_a:
            dict_a[i] = dict_a[i] + 1
            if  dict_a[i] == 2 and first_time:
                result = i
                first_time = False
        else:
            dict_a[i] = 1
    return result

# Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.

# Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.

# There are no characters in this string that do not repeat.

def firstNotRepeatingCharacter(s):
    if len(s) == 1:
        return s
    dict_s = {}
    result = "_"
    first_time = True
    counter = 0
    for c in s:
        if c in dict_s:
            dict_s[c] = dict_s[c] + 1
        else:
            dict_s[c] = 1
    for k in s:
        if dict_s[k] == 1 and first_time:
            result = k
            first_time = False
            counter +=1
    if counter == len(dict_s):
        result = "-"
    return result

# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

# Example

# For

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# the output should be

# rotateImage(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]

def rotateImage(a):
    rotated = list(zip(*reversed(a)))
    return rotated


def main():
    pass

if __name__ == '__main__':
    main()