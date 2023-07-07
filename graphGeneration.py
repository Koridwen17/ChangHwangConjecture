import copy
import numpy as np
import random
from graphTesting import testGraph

def generateAndTestAllGraphs(a, b, m, p, TestComNeighbours = True, TestDeg = True, printGraphs=False):
    couples = []
    for i in range(a):
        for j in range(b):
            couples.append((i,j))
    numgraphs = [0]
    generateAndTestAllGraphsRec(couples, [], a, b, m, p, numgraphs, TestComNeighbours, TestDeg, printGraphs)
    print(numgraphs[0],"graphs tested")

def generateAndTestAllGraphsRec(couples, subset, a, b, m, p, numgraphs, TestComNeighbours, TestDeg, printGraphs):
    if len(couples) < m:
        print ("erreur")
        return
    if len(couples) == m or m == 0:
        if m == 0:
            graph = subset
        else:
            graph = subset + couples
        M = np.zeros((a,b)).astype(int)
        for e in graph:
            M[e[0]][e[1]] = 1
        if printGraphs:
            print(M,"\n")
        numgraphs[0] = numgraphs[0] + 1
        if not testGraph(M,a,b,p):
            print("counter example found: ", M)
    else:
        x = couples.pop()
        subset2 = copy.deepcopy(subset)
        couples2 = copy.deepcopy(couples)
        generateAndTestAllGraphsRec(couples, subset, a, b, m, p, numgraphs, TestComNeighbours, TestDeg, printGraphs)
        subset2.append(x)
        generateAndTestAllGraphsRec(couples2, subset2, a, b, m-1, p, numgraphs, TestComNeighbours, TestDeg, printGraphs)

def generateRandomSomewhatRegularGraph(a, b, m):
    M = np.zeros((a,b)).astype(int)
    Ind = []
    for i in range(b):
        Ind.append(i)
    for k in range(m//a):
        np.random.permutation(Ind)
        for i in range(a):
            x = i
            y = Ind[i]
            if M[x][y] == 0:
                M[x][y] = 1
            else:
                while M[x][y] == 1:
                    y = random.randint(0,b-1)
                M[x][y] = 1
    for k in range(m-m//a*a):
        x = random.randint(0,a-1)
        y = random.randint(0,b-1)
        while M[x][y] == 1:
            x = random.randint(0,a-1)
            y = random.randint(0,b-1)
        M[x][y] = 1
    return M

def createNoise(M,a,b,noise):
    N = copy.deepcopy(M)
    for k in range(noise):
        a1 = random.randint(0,a-1)
        b1 = random.randint(0,b-1)
        a2 = a1
        b2 = b1
        if N[a1][b1] == 0:
            while M[a2][b2] == 0:
                a2 = random.randint(0,a-1)
                b2 = random.randint(0,b-1)
        else:
            while M[a2][b2] == 1:
                a2 = random.randint(0,a-1)
                b2 = random.randint(0,b-1)
        N[a1][b1] = 1 - N[a1][b1]
        N[a2][b2] = 1 - N[a2][b2]
    return N

def generateRandomGraphDegsA(a, b, D): # generate a random graph accordingly to the list of degrees D
    if len(D) != a:
        print("error size of D")
        return
    D2 = [0]*a
    for i in range(a):
        D2[i] = b - D[i]
    M = np.ones((a,b))
    M = M.astype(int)
    for i in range(a):
        for j in range(D2[i]):
            x = random.randint(0, b-1)
            while M[i][x] == 0:
                x = random.randint(0, b-1)
            M[i][x] = 0
    return M

from AllGraphsDegsA_utils import *

def generateAndTestAllGraphsDegsA(a, b, m, D): # generate every graph accordingly to the list of degrees D
    M = baseGraph(a, b, D)
    i = 0
    while len(M) != 0:
        i = i+1
        if i%10000 == 0:
            print(i,"graphs tested")
        M = nextDistribution(M, a, b, D)
        if not testGraph(M, a, b, m//2):
            print("counter example found: ", M)
