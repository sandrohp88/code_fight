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

def main():
    # print(reachNextLevel(10,15,4))
    print(knapsackLight(10,5,6,4,9))

if __name__ == '__main__':
    main()