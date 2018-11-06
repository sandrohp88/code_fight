def extractMatrixColumn(matrix, column):
    return [l[column] for l in matrix]


def areIsomorphic(array1, array2):
    if len(array1) != len(array2):
        return False
    len_array = []
    for i in range(len(array1)):
        len_array.append([len(array1[i]), len(array2[i])])
    for l in len_array:
        if l[0] != l[1]:
            return False
    return True


def swapDiagonals(matrix):
    left_diag = [matrix[i][i] for i in range(len(matrix))]
    right_diag = [matrix[len(matrix) - 1 - i][i]
                  for i in range(len(matrix) - 1, -1, -1)]
    for i in range(len(matrix)):
        matrix[i][i] = right_diag[i]
        matrix[i][len(matrix[i]) - i - 1] = left_diag[i]
    return matrix


def crossingSum(matrix, a, b):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == a or j == b:
                result += matrix[i][j]
    return result


def reverseOnDiagonals(matrix):
    left_diag = [matrix[i][i] for i in range(len(matrix))]
    right_diag = [matrix[len(matrix) - 1 - i][i]
                  for i in range(len(matrix) - 1, -1, -1)]
    left_diag.reverse()
    right_diag.reverse()
    for i in range(len(matrix)):
        matrix[i][i] = left_diag[i]
        matrix[i][len(matrix[i]) - i - 1] = right_diag[i]

    return matrix


def drawRectangle(canvas, rectangle):
    x1, y1, x2, y2 = rectangle
    canvas[y1][x1] = '*'
    canvas[y2][x2] = '*'
    canvas[y2][x1] = '*'
    canvas[y1][x2] = '*'
    for i in range(1, x2 - x1):
        canvas[y1][x1+i] = '-'
        canvas[y2][x1+i] = '-'
    for j in range(1, y2 - y1):
        canvas[y1+j][x1] = '|'
        canvas[y1+j][x2] = '|'

    return canvas


def volleyballPositions(formation, k):

    return formation


def main():
    formation = [["empty",   "Player5", "empty"],
                 ["Player4", "empty",   "Player2"],
                 ["empty",   "Player3", "empty"],
                 ["Player6", "empty",   "Player1"]]
    k = 4
    print(volleyballPositions(formation, k))
    # canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
    #           ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
    #           ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
    #           ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    #           ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
    # rectangle = [1, 1, 4, 3]
    # print(drawRectangle(canvas, rectangle))
    # matrix = [[1, 1, 1, 1],
    #           [2, 2, 2, 2],
    #           [3, 3, 3, 3]]
    # print(crossingSum(matrix, 1, 3))

    # array1 = [[1, 1, 1],
    #           [0, 0],
    #           [0, 0, 0],
    #           [0, 0, 0]]
    # array2 = [[2, 1, 1],
    #           [2, 1],
    #           [0, 0, 0],
    #           [0, 0, 0]]
    # print(areIsomorphic(array1, array2))
    # matrix = [[1, 1, 1, 2],
    #           [0, 5, 0, 4],
    #           [2, 1, 3, 6]]
    # print(extractMatrixColumn(matrix, 1))


if __name__ == '__main__':
    main()
