# Chalenge remove rows and columns
import numpy as np
def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    matrix = np.array(matrix)
    i = 0
    while i < len(rowsToDelete):
        if i == 0:
            matrix = np.delete(matrix,rowsToDelete[i],0)
        else:
             matrix = np.delete(matrix,rowsToDelete[i] -1 ,0)
        i += 1
    i = 0
    while i < len(columnsToDelete):
        if i == 0:
            matrix = np.delete(matrix,columnsToDelete[i],1)
        else:
             matrix = np.delete(matrix,columnsToDelete[i] - 1,1)
        i += 1
    return matrix.tolist()