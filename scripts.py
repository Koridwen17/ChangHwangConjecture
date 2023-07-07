#%% 
# generate all bipartite graphs with parts of size a and b with m edges, and check if they verify the conjecture
# unusable for m above 2^4
from graphGeneration import generateAndTestAllGraphs
import time
a = 4
b = 5
m = 16
t = time.time()
generateAndTestAllGraphs(a, b, m, m//2, TestDeg=False, printGraphs=False)
print("time elapsed:", time.time() - t, "seconds")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# prints every multiset of size a with integers between 0 and b that sums to m while not containing a subset that sums to p
# useful for obtaining interesting lists of the degrees of the vertices in A
from sums import print_all_sum

m = 16 # number of edges of the base graph
a = 5  # size of A
b = 5  # size of B
p = 8  # number of edges of subgraph sought
print_all_sum(m,a,b,p)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# using the lists obtained above, we can test graphs that verify a set repartition D of the degrees of vertices in A:
from graphGeneration import generateRandomGraphDegsA
from graphTesting import testGraph
import time

# testing n random graphs
a = 8
b = 10
m = 64
p = 32
D = [6, 6, 7, 9, 9, 9, 9, 9]
n = 100000

assert len(D) == a, "D is not the size of a"
sum = 0
for i in range(len(D)):
    assert D[i]>=0 and D[i]<=b, "value " + str(i) + " of D is not between 0 and b"
    sum = sum + D[i]
assert sum == m, "sum of degrees is not equal to m"


t = time.time()
for i in range(n):
    M = generateRandomGraphDegsA(a,b,D)
    if not testGraph(M,a,b,p):
        print("counter example found: ", M)
print("time elapsed:", time.time() - t, "seconds")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# or testing all the graphs
from graphGeneration import generateAndTestAllGraphsDegsA
import time
a = 5
b = 5
m = 16
p = 8
D = [3, 3, 3, 3, 4]

assert len(D) == a, "D is not the size of a"
sum = 0
for i in range(len(D)):
    assert D[i]>=0 and D[i]<=b, "value " + str(i) + " of D is not between 0 and b"
    sum = sum + D[i]
assert sum == m, "sum of degrees is not equal to m"


t = time.time()
generateAndTestAllGraphsDegsA(a, b, m, D)
print("time elapsed:", time.time() - t, "seconds")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# generate a random graph with m edges and give a subgraph with m/2 edges
from graphGeneration import generateRandomSomewhatRegularGraph
from graphTesting import testGraphGiveSubgraph
a = 10
b = 10
m = 64
M = generateRandomSomewhatRegularGraph(a, b, m)
print("Random graph with",m,"edges\n",M)
testGraphGiveSubgraph(M, a, b, m//2)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# counter example if the number of edges is not a power of 2: K5,9 plus a disjoint edge
from graphTesting import testGraph
import numpy as np

m = 46
a = 6
b = 10
M = np.zeros((a,b)).astype(int)
M[1:,1:] = 1
M[0,0] = 1
print(M)
print(testGraph(M,a,b,m//2))
