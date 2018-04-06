# You are given a two-digit integer n. Return the sum of its digits.
# Example
# For n = 29, the output should be
# addTwoDigits(n) = 11.
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] integer n
# A positive two-digit integer.
# Guaranteed constraints:
# 10 ≤ n ≤ 99.
# [output] integer
# The sum of the first and second digits of the input number.
def addTwoDigits(n):
    s = str(n)
    a = int(s[0])
    b = int(s[1])
    return(a+b)

# Given an integer n, return the largest number that contains exactly n digits.

# Example

# For n = 2, the output should be
# largestNumber(n) = 99.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n ≤ 9.

# [output] integer

# The largest integer of length n.

def largestNumber(n):
    s = ""
    for i in range(n):
        s += "9"
        i += 1
    return int(s)

# n children have got m pieces of candy.
# They want to eat as much candy as they can,
# but each child must eat exactly the same amount of
# candy as any other child. Determine how many pieces
# of candy will be eaten by all the children together.
# Individual pieces of candy cannot be split.

# Example

# For n = 3 and m = 10, the output should be
# candies(n, m) = 9.

# Each child will eat 3 pieces. So the answer is 9.

def candies(n, m):
    return (m//n) * n

#Your friend advised you to see a new performance in the most popular
# theater in the city. He knows a lot about art and his advice is usually good,
# but not this time: the performance turned out to be awfully dull. It's so bad
# you want to sneak out, which is quite simple, especially since the exit is located
# right behind your row to the left. All you need to do is climb over your seat and
# make your way to the exit.

# The main problem is your shyness: you're afraid that you'll end up blocking
# the view (even if only for a couple of seconds) of all the people who sit
# behind you and in your column or the columns to your left. To gain some courage,
# you decide to calculate the number of such people and see if you can possibly
# make it to the exit without disturbing too many people.

# Given the total number of rows and columns in the theater (nRows and nCols, respectively),
# and the row and column you're sitting in, return the number of people who sit strictly behind
# you and in your column or to the left, assuming all seats are occupied.

# Example

# For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be
# seatsInTheater(nCols, nRows, col, row) = 96.

# Here is what the theater looks like:

def seatsInTheater(nCols, nRows, col, row):
    a = nCols - col
    b = nRows - row
    return a * b + b

# Given a divisor and a bound, find the largest integer N such that:

# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.

# Example

# For divisor = 3 and bound = 10, the output should be
# maxMultiple(divisor, bound) = 9.

# The largest integer divisible by 3 and not larger than 10 is 9.

def maxMultiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    else:
        return bound//divisor * divisor

# Consider integer numbers from 0 to n - 1 written down along
# the circle in such a way that the distance between any two
# neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

# Given n and firstNumber, find the number which is written in the radially
# opposite position to firstNumber.

# Example

# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.
def circleOfNumbers(n, firstNumber):
    if firstNumber >=n//2:
        return firstNumber - n//2
    return firstNumber + n//2

# One night you go for a ride on your motorcycle.
# At 00:00 you start your engine, and the built-in
# timer automatically begins counting the length of your ride,
# in minutes. Off you go to explore the neighborhood.

# When you finally decide to head back, you realize there's a
# chance the bridges on your route home are up, leaving you stranded!
# Unfortunately, you don't have your watch on you and don't know what time it is.
# All you know thanks to the bike's timer is that n minutes have passed since 00:00.

# Using the bike's timer, calculate the current time.
# Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

# Example

# For n = 240, the output should be
# lateRide(n) = 4.

# Since 240 minutes have passed, the current time is 04:00.
# The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

# For n = 808, the output should be
# lateRide(n) = 14.

# 808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
def lateRide(n):
    hours = n // 60
    minutes = n % 60
    str_hours_minutes = str(hours)
    str_hours_minutes += str(minutes)
    result = 0
    for s in str_hours_minutes:
        result += int(s)
    return result

# Some phone usage rate may be described as follows:

# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration
# of the longest call (in minutes rounded down to the nearest integer) you can have?

# Example

# For min1 = 3, min2_10 = 1, min11 = 2 and s = 20, the output should be
# phoneCall(min1, min2_10, min11, s) = 14.

# Here's why:

# the first minute costs 3 cents, which leaves you with 20 - 3 = 17 cents;
# the total cost of minutes 2 through 10 is 1 * 9 = 9, so you can talk 9 more
# minutes and still have 17 - 9 = 8 cents;
# each next minute costs 2 cents, which means that you can talk 8 / 2 = 4 more minutes.
# Thus, the longest call you can make is 1 + 9 + 4 = 14 minutes long.

def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        return 0
    s -= min1
    counter = 1
    minute_interval = 2
    min = min2_10
    while s >= min:
        if minute_interval in range(2,11,1):
            s -= min2_10
            counter += 1
        if minute_interval in range(11,1000,1):
            s-=min11
            counter += 1
            min = min11
            
        minute_interval += 1
    return counter


def main():
    pass

if __name__ == '__main__':
    main()