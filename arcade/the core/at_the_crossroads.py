# You are playing an RPG game. Currently your experience points (XP) total is equal to experience.
# # To reach the next level your XP should be at least at threshold. If you kill the monster in front
#  of you, you will gain more experience points in the amount of the reward.

# Given values experience, threshold and reward, check if you reach the next level after killing the monster.

# Example

# For experience = 10, threshold = 15 and reward = 5, the output should be
# reachNextLevel(experience, threshold, reward) = true;
# For experience = 10, threshold = 15 and reward = 4, the output should be
# reachNextLevel(experience, threshold, reward) = false.

def reachNextLevel(experience, threshold, reward):
    next_level = (experience + reward) >= threshold
    return next_level

# You found two items in a treasure chest! The first item weighs weight1 and is worth value1,
# # and the second item weighs weight2 and is worth value2. What is the total maximum value
# # of the items you can take with you, assuming that your max weight capacity is maxW and
#  you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type,
#  i.e. you can't take two first items or two second items.

# Example

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

# You can only carry the first item.

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

# You're strong enough to take both of the items with you.

# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4 and maxW = 6, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

# You can't take both items, but you can take any of them.

def knapsackLight(value1, weight1, value2, weight2, maxW):
    
    if weight1 > maxW and weight2 > maxW:
        return 0
    # If maxW is less than weight1 + weight2 
    # return the sum of the value1 + value2
    if (weight1 + weight2) <= maxW:
        return value1 + value2

    if weight1 > weight2:
        if weight1 <= maxW and value1 > value2:
            return value1
        else:
            return value2

    else:
        if weight2 <= maxW and value2 > value1:
            return value2
        else:
            return value1

# You're given three integers, a, b and c. It is guaranteed
# that two of these integers are equal to each other.
# What is the value of the third integer?
# Example
# For a = 2, b = 7 and c = 2, the output should be
# extraNumber(a, b, c) = 7.
# The two equal numbers are a and c. The third number (b) equals 7, which is the answer.

def extraNumber(a, b, c):
    if a == b:
        return c
    if a == c:
        return b
    return a

# Given integers a and b, determine whether the 
# following pseudocode results in an infinite loop

# while a is not equal to b do
#   increase a by 1
#   decrease b by 1
# Assume that the program is executed on a virtual machine 
# which can store arbitrary long numbers and execute forever.

# Example

# For a = 2 and b = 6, the output should be
# isInfiniteProcess(a, b) = false;
# For a = 2 and b = 3, the output should be
# isInfiniteProcess(a, b) = true.

def isInfiniteProcess(a, b):
    if a == b:
        return False
    if a < b:
        while a <= b:
            if a == b:
                return False
            else:
                a += 1
                b -= 1
                   
                    
    return True

# Consider an arithmetic expression of the form a#b=c. 
# Check whether it is possible to replace # with one of 
# the four signs: +, -, * or / to obtain a correct expression.

# Example

# For a = 2, b = 3 and c = 5, the output should be
# arithmeticExpression(a, b, c) = true.

# We can replace # with a + to obtain 2 + 3 = 5, so the answer is true.

# For a = 8, b = 2 and c = 4, the output should be
# arithmeticExpression(a, b, c) = true.

# We can replace # with a / to obtain 8 / 2 = 4, so the answer is true.

# For a = 8, b = 3 and c = 2, the output should be
# arithmeticExpression(a, b, c) = false.

# 8 + 3 = 11 ≠ 2;
# 8 - 3 = 5 ≠ 2;
# 8 * 3 = 24 ≠ 2;
# 8 / 3 = 2.(6) ≠ 2.
# So the answer is false.

def arithmeticExpression(a, b, c):
    if (a + b == c):
        return True
    if (a - b == c):
        return True
    if (a / b == c):
        return True
    if (a * b == c):
        return True
    return False

# In tennis, a set is finished when one of the players wins 6 games 
# and the other one wins less than 5, or, if both players win at 
# least 5 games, until one of the players wins 7 games.

# Determine if it is possible for a tennis set to be finished with 
# the score score1 : score2.

# Example

# For score1 = 3 and score2 = 6, the output should be
# tennisSet(score1, score2) = true.

# For score1 = 8 and score2 = 5, the output should be
# tennisSet(score1, score2) = false.

# Since both players won at least 5 games, the set would've ended once one of them won the 7th one.

# For score1 = 6 and score2 = 5, the output should be
# tennisSet(score1, score2) = false.

def tennisSet(score1, score2):
    winning_number = 6
    if score1 >= 5 and score2 >= 5:
        if score1 == score2:
            return False
        else:
            winning_number = 7
    if score1 == winning_number or score2 == winning_number:
        return True
    else:
        return False
   

def main():
    # print(reachNextLevel(10,15,4))
    #  print(knapsackLight(10,5,6,4,9))
    # print(isInfiniteProcess(2,3))
    print(tennisSet(5,8))

if __name__ == '__main__':
    main()