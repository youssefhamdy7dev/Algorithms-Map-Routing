# Imports
from numpy import Inf
import math
import heapq
import time
# Functionalities
# Dijkstra Optimization Idea: Avoid ReInitializing each query.
def  dijkstraToOrigin (dijkstra , changes):
    for i in changes:
        dijkstra[i]      = Inf
    return dijkstra

def  visitedToOrigin (visited , changes):
    for i in changes:
        visited[i] = False
    return  visited

# Node Node -> Number
# consumes Two tuple nodes in the form (X coor, Y coor)
# produces the Eucledian Space of Those given Two nodes.
#  spec: it rounds the numbers to Sig. one digit.
def euclidean_distance(n1, n2):
    d = math.sqrt( (n2[1]-n1[1])**2 + (n2[0]-n1[0])**2 )
    return  round(d, 1)

# takes a file name 'with its full path'
# produces an array of all lines
# spec: it discards any empty line
def read_txt_file(relativefilepath):
    file_handndler = open(relativefilepath)
    lines = []
    for line in file_handndler:
        if line.strip():
            line = [int(i) for i in line.split()]
            lines.append(line)
    file_handndler.close()
    return lines

# (Listof  Integer), Integer ->  -
# consumes a listof Integers to print at one line and a second Integer value to print into a second line
# produces nothing
# spec: it prints a new line at very end.
def write_to_txt(outputFileHandler, firstLine, secondLine):
    for i in range(len(firstLine)):
        outputFileHandler.write(str(firstLine[i])+'  ')
    outputFileHandler.write('\n')
    outputFileHandler.write(str(secondLine))
    outputFileHandler.write('\n')
# ==
