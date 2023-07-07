from sums import isThereSubsetSum, giveSubsetSum
from sympy.combinatorics import GrayCode
from bitarray import bitarray
import numpy as np


def testGraph(M, a, b, p, testComNeighbours=True, testDeg=True): # check if such a subgraph exists without returning it
    if testComNeighbours:
        if testNeighbour(M,a,b):
            #print("no common neighbour")
            return True
    if testDeg:
        for i in range(a):
            deg = degre(M,i,0)
            if deg == 0 or deg >= p-4:
                return True
        for i in range(b):
            deg = degre(M,i,1)
            if deg == 0 or deg >= p-4:
                return True
    if testSubsetSum(M,a,b,p):
        #print("subgraph found")
        return True
    return False

def testGraphGiveSubgraph(M, a, b, p): # almost like testGraph but also gives the solution
    (a,b) = (min(a,b),max(a,b))
    x = GrayCode(a, start = '1'*(a))
    n = x.selections
    for ind in range (1,n): #les A'
        if ind%8192 == 0:
            print(float(ind)/float(n))
        ASubset = bitarray(x.next(ind).current)
        Bdegres = [0]*b
        for j in range(b):
            deg = 0
            for i in range(a):
                if ASubset[i] == 1 and M[i][j] == 1:
                    deg = deg+1
            Bdegres[j] = deg
        BSubset = [0]*b
        giveSubsetSum(Bdegres, p,BSubset)
        if len(BSubset) != 0:
            print("\nA subset: ", ASubset.tolist())
            print("B subset: ", BSubset)
            N = np.zeros((a,b)).astype(int)
            s = 0
            for i in range(a):
                if ASubset[i] == 1:
                    for j in range(b):
                        if BSubset[j] == 1:
                            N[i][j] = M[i][j]
                            s = s + M[i][j]
            print("\nSubgraph found,",s,"edges:\n",N)
            return
    print("no subgraph found")

# For every subset A' of A, check if there exists B' a subset of B such that the induced subgraph (A',B') contains p edges.
# To do so we calculate the degrees of the vertices in B from the induced subgraph (A',B) 
# and solve the subset sum problem in pseudo polynomial time
def testSubsetSum(M, a, b, p): 
    (a,b) = (min(a,b),max(a,b))
    x = GrayCode(a, start = '0'*(a))
    n = x.selections
    for ind in range (1,n): #les A'
        if ind%8192 == 0:
            print(float(ind)/float(n))
        ASubset = bitarray(x.next(ind).current)
        Bdegres = [0]*b
        for j in range(b):
            deg = 0
            for i in range(a):
                if ASubset[i] == 1 and M[i][j] == 1:
                    deg = deg+1
            Bdegres[j] = deg
        if isThereSubsetSum(Bdegres, p):
            #print(ASubset)
            return True
    return False     

def testNeighbour(M,a,b):
    for i in range(b):
        deg = degre(M,i,1)
        if deg == 0:
            return 'deg 0'
    for u in range(a):
        for v in range(u+1,a):
            if not hasCommonNeighbour(M,u,v,0):
                return False
    for u in range(b):
        for v in range(u+1,b):
            if not hasCommonNeighbour(M,u,v,1):
                return False
    return True

def hasCommonNeighbour(M,u,v,nb): # for a graph M and 2 vertices u and v, checks if u and v have a common neighbour
    if nb == 0:
        if u<len(M) and v<len(M):
            for i in range(len(M[u])):
                if M[u][i] == 1 and M[v][i] == 1:
                    return True
            return False
    if nb == 1:
        if u<len(M[0]) and v<len(M[0]):
            for i in range(len(M)):
                if M[i][u] == 1 and M[i][v] == 1:
                    return True
            return False

def degre(M,i,nb): # returns the degree of a vertex
    deg = 0
    if nb == 0:
        for j in range(len(M[i])):
            deg = deg + M[i][j] 
    if nb == 1:
        for j in range(len(M)):
            deg = deg + M[j][i] 
    return deg