# Several people are standing in a row and need to be divided into two teams. 
# The first person goes into team 1, the second goes into team 2, the third 
# goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. 
# Return an array of two integers, where the first element is the total weight 
# of team 1, and the second element is the total weight of team 2 after the division is complete.

# Example

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].
def alternatingSums(a):
    #
    team_one = []
    team_two = []
    
    for i in range(0, len(a),2):
        team_one.append(a[i])
    
    for i in range(1, len(a),2):
        team_two.append(a[i])
    result = []
    result.append(sum(team_one))
    result.append(sum(team_two))
    return result

# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    string_len = len(picture[0])
    asterisk = '*' * (string_len + 2)
    for i in range(len(picture)):
        new_string = picture[i]
        new_string = '*' + new_string
        new_string = new_string + '*'
        picture[i] = new_string
    
    picture.insert(0,asterisk)
    picture.append(asterisk)
    return picture

# Two arrays are called similar if one can be obtained 
# from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# Example

# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.

# The arrays are equal, no need to swap any elements.

# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.

# We can obtain b from a by swapping 2 and 1 in b.

# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.

# Any swap of any two elements either in a or in b won't make a and b equal.
def areSimilar(a, b):
    # Save the indexs wich differ
    indexs = []
    for i in range(len(a)):
        if a[i] != b[i]:
            indexs.append(i)
    # Return True are equals
    if len(indexs) == 0:
        return True
    # If there are one or more than two differences it can't be similar
    if len(indexs) > 2 or len(indexs) == 1 :
        return False
    else: 
        # Two elements differents
        # Swap them and check if the array remains equals  
        b[indexs[0]] , b[indexs[1]] = b[indexs[1]] , b[indexs[0]]
        return a == b 

# You are given an array of integers. On each move you are allowed to 
# increase exactly one of its element by one. Find the minimal number 
# of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

def arrayChange(inputArray):
    #
    minimum_sum = 0
    i = 0
    while i < len(inputArray) - 1:
        if inputArray[i] >= inputArray[i + 1]:
            difference = inputArray[i] - inputArray[i + 1] + 1
            minimum_sum += difference
            inputArray[i+1] += difference
        i += 1
    return minimum_sum

# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.
def palindromeRearranging(inputString):
    #
    character_count = {}
    for i in range(len(inputString)):
        if inputString[i] in character_count.keys():
            character_count[inputString[i]] += 1
        else:
            character_count[inputString[i] ] = 1

    if len(inputString) % 2 == 0:
        for key in character_count.keys():
            if character_count[key] % 2 != 0:
                return False
        return True
    else:
        odd_counter = 0
        for key in character_count.keys():
            if character_count[key] % 2 != 0:
                odd_counter += 1
            if odd_counter > 1:
                return False
        return True

def main():
    # a = [50, 60, 60, 45, 70]
    # print(alternatingSums(a))
    # picture = ["abc",
    #         "ded"]
    # print(addBorder(picture))

    # a = [1, 2, 3] 
    # b = [1, 1, 3]
    # print(areSimilar(a,b))
    # inputArray = [1, 1, 1]
    # print(arrayChange(inputArray))
    inputString = "aabb"
    print(palindromeRearranging(inputString))

if __name__ == '__main__':
    main()