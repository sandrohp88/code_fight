
# Billy and Mandy are twins, and as such they do everything together. Unfortunately during the finals they were forced to write their exams separately, which explains why they got such low scores. However, they are not too sad about it: since they are twins, it's only natural for them to work together, so they are going to sum up their scores for each exam and show them to their mom.

# Given two lists of equal size representing the scores Billy and Mandy got for each exam (b and m, respectively), return a single list containing their combined score.

# Example

# For b = [22, 13, 45, 32] and m = [28, 41, 13, 32],
# the output should be
# twinsScore(b, m) = [50, 54, 58, 64].

def twinsScore(b, m):
    return [b[i] + m[i] for i in range(len(b))]

# Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, and his task is to check the gauges twice a day. By analyzing the morning and evening pressures of each pipe, Harry should write a report about the minimum and the maximum pressure during the day.

# Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, and the second one containing the maximum pressure of each pipe during the day.

# Example

# For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6],
# the output should be
# pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].

def pressureGauges(morning, evening):
    return [[ min(morning[i], evening[i])    for i in range(len(morning))] ] + [[ max(morning[j], evening[j])    for j in range(len(morning))]]
# For the opening ceremony of the upcoming sports event an even number of athletes were picked. They formed a correct lineup, i.e. such a lineup in which no two boys or two girls stand together. The first person in the lineup was a girl. As a part of the performance, adjacent pairs of athletes (i.e. the first one together with the second one, the third one together with the fourth one, etc.) had to swap positions with each other.

# Given a list of athletes, return the list of athletes after the changes, i.e. after each adjacent pair of athletes is swapped.

# Example

# For athletes = [1, 2, 3, 4, 5, 6], the output should be
# correctLineup(athletes) = [2, 1, 4, 3, 6, 5]

def correctLineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]
 
# You're organizing a group dating activity for cats, i.e. a meeting where an equal number of male and female cats get together. For each cat you calculate their nature value, an integer that describes the cat's spirit. When a male and a female cat with the same nature value see each other, they become connected and happily walk out together.

# You've just started another group dating, and placed the cats in front of one another so that the ith male is sitting across the ith female. What cats will remain at their places, assuming that the pairs of cats sitting in front of each other and having the same nature values will walk out?

# Example

# For male = [5, 28, 14, 99, 17] and
# female = [5, 14, 28, 99, 16],
# the output should be
# groupDating(male, female) = [[28, 14, 17], [14, 28, 16]].

# Pairs of cats at positions 0 and 3 (0-based) have the same nature values, so they will leave the meeting.
def groupDating(male, female):
    return [ [male[i] for i in range(len(male)) if male[i] != female[i]]]   +  [[female[i] for i in range(len(male)) if male[i] != female[i]] ]

# Unfortunately because of the extreme coldness the tree that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given tree by centering the asterisks in each line.

# Example

# For

# tree = [
#   "      *  ", 
#   "    *    ", 
#   "***      ", 
#   "    *****", 
#   "  *******", 
#   "*********", 
#   " ***     "
# ]
# the output should be

# fixTree(tree) = [
#   "    *    ", 
#   "    *    ", 
#   "   ***   ", 
#   "  *****  ", 
#   " ******* ", 
#   "*********", 
#   "   ***   "
# ]

def fixTree(tree):
    return [' '*((len(s) - len(s.strip())) // 2 ) + '*'*(len(s.strip())) + ' '*((len(s) - len(s.strip())) // 2) for s in tree]

# There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

# Example

# For a = [1, 2, 3], the output should be
# prefSum(a) = [1, 3, 6].

# Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].

from numpy import cumsum

def prefSum(a):
    return list(cumsum(a))

# Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of numbers, Billy should calculate the following value:

# (((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
# Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of numbers, will return the result of the operation Billy has to perform.

# Example

# For numbers = [1, 2, 3, 4, 5, 6], the output should be
# mathPractice(numbers) = 71.

# Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.
from functools import reduce

def mathPractice(numbers):
    # for element in it:
    #     value = function(value, element)
    return reduce(lambda a,b: a*b[1] if b[0] % 2 == 0 else a+b[1]  ,enumerate(numbers),1 )

# You're organizing murder mystery games for your coworkers, and came up with a lot of ideas for various groups of participants. The ith 0-based game can be played only if there are at least i people registered for it. Game number 0 is a beta that you will try out with your friends, so there's no need for participants.

# You're expecting a full house, since a lot of participants signed up already. Not too many, unfortunately: looks like some games can't be played, because too few people registered for them. Given the list of participants, your task is to return the list of games for which too few people signed up.

# Example

# For participants = [0, 1, 1, 5, 4, 8], the output should be
# checkParticipants(participants) = [2].

# For the game number 2 (0-based) 2 people are required, but only one person has registered.
def checkParticipants(participants):
    return [i for i,j in enumerate(participants) if i > j and i > 0]

# No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 3, 5, ..., in other words those whose length increase according to the Fibonacci sequence.

# The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer n, return a list of n lists, where the first element consists is empty (consists of 0 zeros), the second element consists of 1 zero, and so on.

# Example

# For n = 6, the output should be

# fibonacciList(n) = [[], 
#                     [0], 
#                     [0], 
#                     [0, 0], 
#                     [0, 0, 0], 
#                     [0, 0, 0, 0, 0]]
from functools import reduce

def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x,y: [0] if y== 0 else (x + [1] if y in[1,2]   else x + [x[-1]+ x[-2]]) ,range(n),[])]
# It is believed by some tribes of South Codelenica that only two events determine the person's destiny: the first time he picked a flower, and the first time he planted one. They also believe in the power of prime numbers and in the power of sums (and a bunch of other most probably unrelated stuff), so you are wondering if it has something to do with their belief in the destiny-determining events.

# You know that you first picked a flower in year a of the Codelenican calendar, and planted it in year b. Now you're curious about the sum of all the prime numbers in the range [a, b], to see if this number could possibly affect your life.

# Example

# For a = 10 and b = 20, the output should be
# primesSum(a, b) = 60.

# There are 4 prime numbers in the range [10, 20]: 11, 13, 17 and 19. Their sum is equal to 11 + 13 + 17 + 19 = 60. It's a round number, maybe it does mean something?..
def primesSum(a, b):
    for i in range(2,1):
        print(i)
    return [p  for p in range(a,b + 1) if all(p%p1 != 0  for p1 in range(2,p)) and p != 1]
def main(): 
    a,b = 1,7
    print(primesSum(a, b))
    # numbers = [1, 2, 3, 4, 5, 6]
    # print(mathPractice(numbers))
    # morning = [3, 5, 2, 6]
    # evening = [1, 6, 6, 6]
    # print(pressureGauges(morning,evening))
    # athletes = [1, 2, 3, 4, 5, 6]
    # print(correctLineup(athletes))
    # male = [5, 28, 14, 99, 17]
    # female = [5, 14, 28, 99, 16]
    # print(groupDating(male, female))
#     tree = [
#    "      *  ", 
#    "    *    ", 
#    "***      ", 
#    "    *****", 
#    "  *******", 
#    "*********", 
#    " ***     "
#  ]
#     print(fixTree(tree))
    # a = [1, 2, 3]
    # print(prefSum(a))


if __name__ == '__main__':
    main()