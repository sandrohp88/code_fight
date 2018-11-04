import itertools
from collections import defaultdict

def sugarHigh(candies, threshold):
    if sum(candies) <= threshold:
        return list(range(len(candies)))
    candies_index = list()
    for index, candie in enumerate(candies):
        candies_index.append([index, candie])
    candies_index = sorted(candies_index, key=lambda c_index: c_index[1])
    indexes_list = list()
    result = list()
    acc = 0
    for c_i in candies_index:
        acc += c_i[1]
        if acc <= threshold:
            indexes_list.append(c_i[0])
        else:
            result.append(sorted(indexes_list))
            indexes_list = list()
            acc = 0
    result = sorted(result, key=len, reverse=True)
    print(result)
    return [] if len(result) < 1 else result[0]


def combinations(iterable, r, threshold):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    result = []
    if r > n:
        return
    indices = list(range(r))
    possiTuple = list(pool[i] for i in indices)
    if sum(possiTuple) <= threshold:
        result.append([possiTuple, list(indices)])
        # print(possiTuple, indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return result
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        possiTuple = list(pool[i] for i in indices)
        if sum(possiTuple) <= threshold:
            result.append([possiTuple, list(indices)])
            # print(possiTuple, indices)
    return result


def sugarHighBruteForce(candies, threshold):
    i = len(candies)
    result = []
    while i > 0 and len(result) < 3:
        comb = combinations(candies, i, threshold)
        comb = sorted(comb, key=cmp_to_key(cmp_sugar))
        if len(comb) > 0:
            result.append(comb)
        i -= 1
    # print(result[0][0][1])
    return [] if len(result) < 1 else result[0][0][1]


def cmp_sugar(sugar1, sugar2):
    valuesS1 = sugar1[0]
    indexesS1 = sugar1[1]

    valuesS2 = sugar2[0]
    indexesS2 = sugar2[1]

    if len(valuesS1) == len(valuesS2) and sum(valuesS1) == sum(valuesS2):
        if sum(indexesS1) == sum(indexesS2):
            return 0
        elif sum(indexesS1) < sum(indexesS2):
            return -1
        else:
            return 1
    if len(valuesS1) == len(valuesS2):
        return -1 if sum(valuesS1) < sum(valuesS2) else 1

    return -1 if len(valuesS1) < len(valuesS2) else 1


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def main():
    candies = [8, 68, 32, 28, 90, 19, 25, 44, 83, 49]
    threshold = 250
    print(sugarHigh(candies, threshold))


if __name__ == '__main__':
    main()
