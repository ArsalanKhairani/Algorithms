################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Matrix Multiplication                             ##
##                                                                            ##
## Trivial Method of applying two matrices. Matrices are shored as List of    ##
## lists. Let X and Y be two matrices such that order of X is n*m and order   ##
## of Y is m*o. Where n, m and o are integers                                 ##
################################################################################

# Function: Given the two matrices will return the resultant X*Y matrix
# Example : [ 1 2 3 ] * [ 1 2 ]     [ 22 28 ]
#           [ 4 5 6 ]   [ 3 4 ]  =  [ 49 64 ]
#                       [ 5 6 ]
def MatrixMultiplication(X, Y):

    # Base Case
    n = len(X)
    m = len(X[0])
    o = len(Y[0])
    
    Z = [ [ 0 for i in range(o) ] for j in range(n) ]

    # Three nested loops
    for i in range(o):
        for j in range(n):
            for k in range(m):
                Z[i][j] += (X[i][k] * Y[k][j])

    return Z


X = [[1, 2, 3], [4, 5, 6]]
Y = [[1, 2], [3, 4], [5, 6]]
print (MatrixMultiplication(X, Y))
