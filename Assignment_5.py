import numpy

# Constraints
A = numpy.matrix([[1, 1, 1], [3, 2, 1], [0, 0, 1]])
b = [6, 10, 3]

# Determine the solution
x = numpy.linalg.solve(A, b)
