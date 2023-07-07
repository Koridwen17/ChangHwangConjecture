import copy
import numpy as np

def baseGraph(a, b, D):
    M = np.ones((a, b))
    M = M.astype(int)
    for i in range(a):
        for j in range(b-D[i], b):
            M[i][j] = 0
    return M

def nextDistribution(M, a, b, D):
    ind = a
    A = []
    while len(A) == 0:
        ind = ind - 1
        if ind == -1:
            return []
        A = copy.deepcopy(M[ind])
        A = nextDistributionLine(A, b)
    M[ind] = copy.deepcopy(A)
    #print(ind)
    for j in range (ind+1, a):
        for l in range(b-D[j]):
            M[j][l] = 1
        for l in range(b-D[j], b):
            M[j][l] = 0
    return M

def nextDistributionLine(A, b):
    i = b-1
    while A[i] == 1:
        i = i-1
    num1 = 0
    while A[i] ==  0:
        i = i-1
        num1 = num1 + 1
        if i == -1:
            return []
    A[i] = 0
    for j in range(i+1, b-num1+1):
        A[j] = 1
    for j in range(b-num1+1, b):
        A[j] = 0
    return A