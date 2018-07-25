
# You are working on a revolutionary video game. In this game the player will be able to collect several types of bonuses on each level, and his total score for the level is equal to the sum of the first n bonuses he collected. However, if he collects less than n bonuses, his score will be equal to 0.

# Given the bonuses the player got, your task is to return his final score for the level.

# Example

# For bonuses = [4, 2, 4, 5] and n = 3,
# the output should be
# calcBonuses(bonuses, n) = 10.

# 4 + 2 + 4 = 10.

# For bonuses = [4, 2, 4, 5] and n = 5,
# the output should be
# calcBonuses(bonuses, n) = 0.

# The player has collected only 4 bonuses, so his final score is 0.
def calcBonuses(bonuses, n):
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return 
# You are working on a revolutionary video game. This game will consist of several levels, and on each level the player will be able to collect bonuses. For each passed level the player will thus get some score, determined by the number of collected bonuses.

# Player's final score is decided by the number of completed levels and scores obtained on each of them. The final score is calculated as the sum of squares of n maximum scores obtained. If the number of completed levels is less than n, the score is calculated as the sum of squared scores for each level, and final result is divided by 5 as a penalty (the result is rounded down to the nearest integer).

# Given the list of scores the player got for completed levels and the number n that determines the number of levels you have to pass to avoid being penalized, return the player's final game score.

# Example

# For scores = [4, 2, 4, 5] and n = 3,
# the output should be
# calcFinalScore(scores, n) = 57.

# 52 + 42 + 42 = 57.

# For scores = [4, 2, 4, 5] and n = 5,
# the output should be
# calcFinalScore(scores, n) = 12.

# (42 + 22 + 42 + 52) / 5 = 61 / 5 ≈ 12.

def calcFinalScore(scores, n):
    gen = iter([x*x for x in sorted(scores,reverse = True)[:n] ])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res


# Fibonacci sequence is known to every programmer, and you're not an exception. It is believed that not all properties of Fibonacci numbers are yet studied, and in order to help your descendants, you'd like to implement a generator that will generate Fibonacci numbers infinitely. Who knows, maybe in the distant future your generator will help to make a breakthrough in this field!

# To test your generator, you'd like to check the first few values. Given the number n, return the first n numbers of Fibonacci sequence.

# Example

# For n = 3, the output should be
# fibonacciGenerator(n) = [0, 1, 1].

# The first three Fibonacci numbers are 0, 1 and 1.
def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]
# The Calkin-Wilf tree is a tree in which the vertices correspond 1-for-1 to the positive rational numbers. The tree is rooted at the number 1, and any rational number expressed in simplest terms as the fraction a / b has as its two children the numbers a / (a + b) and (a + b) / b. Every positive rational number appears exactly once in the tree. Here's what it looks like:



# The Calkin-Wilf sequence is the sequence of rational numbers generated by a breadth-first traversal of the Calkin-Wilf tree, where the vertices of the same level are traversed from left to right (as displayed in the image above). The sequence thus also contains each rational number exactly once, and can be represented as follows:



# Given a rational number, your task is to return its 0-based index in the Calkin-Wilf sequence.

# Example
# For number = [1, 3], the output should be
# calkinWilfSequence(number) = 3.

# As you can see in the image above, 1 / 3 is the 3rd 0-based number in the sequence.
def calkinWilfSequence(number):
    def fractions():
        r = 0
        l = 0
        count = 0
        left = False
        while True:
            if not left:
                left = True
                left_child = [l,l + r]
                r += 1
            else:
                left = False
                right_child = [l+r,r]
                l += 1
           
            print('{}/{}'.format(left_child[0],left_child[1]))
            # print('{}/{}'.format(right_child[0],right_child[1]))
            yield left_child
            
            

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


def main():
    # bonuses = [4, 2, 4, 5]
    number = [1,3]
    print(calkinWilfSequence(number))    
    # print(calcBonuses(bonuses,3))

if __name__ == '__main__':
    main()