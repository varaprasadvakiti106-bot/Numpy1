#SciPy Getting Started
from scipy import constants
print(constants.liter)

import scipy
print(scipy.__version__)

#Constants in SciPy
print(constants.pi)
#Constant Units
#A list of all units under the constants module can be seen using the dir() function.
print(dir(constants))

#Metric (SI) Prefixes:
#Return the specified unit in meter (e.g. centi returns 0.01)
print(constants.yotta)
print(constants.zetta)
print(constants.exa)
print(constants.peta)
print(constants.tera)
print(constants.giga)
print(constants.mega)
print(constants.kilo)
print(constants.hecto)
print(constants.deka)
print(constants.deci)
print(constants.centi)
print(constants.milli)
print(constants.micro)
print(constants.nano)
print(constants.pico)
print(constants.femto)
print(constants.atto)

#Binary Prefixes:
#Return the specified unit in bytes (e.g. kibi returns 1024)
print(constants.kibi)
print(constants.mebi)
print(constants.gibi)

#Mass:
#Return the specified unit in kg (e.g. gram returns 0.001)
print(constants.gram)
print(constants.kilo)

#Angle:
#Return the specified unit in radians 
print(constants.degree)
print(constants.arcmin)
print(constants.arcsec)

#Time:
#Return the specified unit in seconds
print(constants.minute)
print(constants.hour)
print(constants.day)

#Length:
#Return the specified unit in meters 
print(constants.inch)
print(constants.foot)
print(constants.yard)

#Pressure:
#Return the specified unit in pascals
print(constants.atm)
print(constants.bar)

#SciPy Optimizers
#Roots of an Equation
from scipy.optimize import root
from numpy import cos

def eqn(x):
  return x + cos(x)
myroot = root(eqn, 0)
print("Roots of the equation:", myroot.x)
print(myroot)

#Finding Minima
from scipy.optimize import minimize
def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0 , method='BFGS')
print("Minima : ",mymin)

def eqn (x):
  return x**4 + x + 4
mymin = minimize(eqn, 0 , method='CG')
print("Minima2 : ",mymin)

#SciPy Sparse Data
#CSR Matrix
#We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

arr = np.array([0,0,0,1,0,1,0,2,3])
print(csr_matrix(arr))

#Sparse Matrix Methods
#Viewing stored data (not the zero items) with the data property.
arr1 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr1).data)
#Counting nonzeros with the count_nonzero() method:
arr2 = np.array([[0,0,0],[1,0,1],[1,0,2]])
print(csr_matrix(arr2).count_nonzero())

#Removing zero-entries from the matrix with the eliminate_zeros() method:
arr3 = np.array([[0,0,0],[1,0,1],[1,0,2]])
mat = csr_matrix(arr3)
mat.eliminate_zeros()
print(mat)

#Eliminating duplicate entries with the sum_duplicates() method:
A = np.array([[0,0,0],[0,1,0],[2,0,2]])
mat = csr_matrix(A)
mat.sum_duplicates()
print(mat)

#Converting from csr to csc with the tocsc() method.
B = np.array([[0,0,0],[1,0,1],[2,0,2]])
newarr = csr_matrix(B).tocsc()
print(newarr)

#SciPy Graphs
#Connected Components
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
arr = np.array([
  [0,1,2],
  [1,0,0],
  [2,0,0]
])
new = csr_matrix(arr)
print(connected_components(new))

Arr = np.array([
  [1,0,2],
  [2,1,3],
  [3,0,3]
]) 

new1 = csr_matrix(Arr)
print(connected_components(new1))

#Dijkstra
#Use the dijkstra method to find the shortest path in a graph from one element to another.
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

a = np.array([
  [0,1,2],
  [1,0,0],
  [2,0,0]
])
a1 = csr_matrix(a)
print(dijkstra(a1, return_predecessors=True, indices=0))

#Floyd Warshall
#Use the floyd_warshall() method to find shortest path between all pairs of elements.
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0,1,2],
  [1,0,0],
  [2,0,0]
])

newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))

A = np.array([
  [1,0,3],
  [1,2,0],
  [0,2,3]
])

A1 = csr_matrix(A)
print(floyd_warshall(A1, return_predecessors=True))

#Bellman Ford
#The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
b = np.array([
  [0,-1,2],
  [1,0,0],
  [2,0,0]
])
b2 = csr_matrix(b)
print(bellman_ford(b2, return_predecessors=True, indices=0))

a = np.array([
  [0,1,-2],
  [1,0,0],
  [2,0,0]
])
a1 = csr_matrix(a)
print(bellman_ford(a1, return_predecessors=True,indices=0)) 

#Depth First Order
#Traverse the graph depth first for given adjacency matrix:
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 2))

#Breadth First Order
#The breadth_first_order() method returns a breadth first traversal from a node.
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))

#SciPy Spatial Data
#Create a triangulation from following points:
#KDTrees
from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

res = kdtree.query((1, 1))

print(res)

#Distance Matrix
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(res)

#Cityblock Distance (Manhattan Distance)
#Find the cityblock distance between given points:
from scipy.spatial.distance import cityblock
a = (1,0)
b = (10,2)

c = cityblock(a,b)
print(c)

x = (3,6)
y = (9,5)
z = cityblock(x,y)
print(z)

#Find the cosine distsance between given points:
from scipy.spatial.distance import cosine
a = (1,0)
b = (8,3)
c = cosine(a,b)
print(c)

#Find the hamming distance between given points:

from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)