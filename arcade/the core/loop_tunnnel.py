import itertools

# Given an integer n, find the minimal k such that

# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.

# Example

# For n = 17, the output should be
# leastFactorial(n) = 24.

# 17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

def leastFactorial(n):
    i , k = 1,2
    k = 1
    while k < n:
        k *= i 
        i += 1
    return k
# Given integers n, l and r, find the number of ways
# to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

# Example

# For n = 6, l = 2 and r = 4, the output should be
# countSumOfTwoRepresentations2(n, l, r) = 2.

# There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

def countSumOfTwoRepresentations2(n, l, r):
    if r < n and n - r >l :
        l = n - r
        r = n - l
    else:
        r = n - l 
        l = n - r
    counter = 0
    while l <= r:
        counter += 1
        print(l,r)
        l += 1
        r -= 1
    return counter
# You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make?

# Example

# For a = 1, b = 2 and n = 2, the output should be
# magicalWell(a, b, n) = 8.

# You will cast your first marble and get $2, after which the numbers will become 2 and 3. When you cast your second marble, the well will give you $6. Overall, you'll make $8. So, the output is 8.
def magicalWell(a, b, n):
    result = 0
    for _ in range(1,n+1):
        result += a*b
        a += 1
        b += 1
    return result


def main():
    print(magicalWell(1,2,2))
    #print(leastFactorial(17))
    #print(factorial(120))
    # print(countSumOfTwoRepresentations2(1000000,490000,900000))

if __name__ == '__main__':
    main()