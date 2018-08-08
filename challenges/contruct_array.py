# Given an integer size, return an array containing each integer from 1 to size in the following order:
# 1, size, 2, size - 1, 3, size - 2, 4, ...
# Example
# For size = 7, the output should be
# constructArray(size) = [1, 7, 2, 6, 3, 5, 4].
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] integer size
# A positive integer.
# Guaranteed constraints:
# 1 ≤ size ≤ 15.
# [output] array.integer


def constructList(size):
    result = []
    i = 0
    while size - i != i + 1 and size - i > i and i in range(size):
        result.append(i + 1)
        result.append(size - i)
        i += 1

    if size - i == i + 1:
        result.append(i + 1)
    return result


def main():
    print(constructList(7))


if __name__ == '__main__':
    main()
