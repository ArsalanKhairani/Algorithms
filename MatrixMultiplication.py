# Applying matrix multiplication 7:52
# Applying with list of lists

def MatrixMultiplication(X, Y):

    # Base Case
    if len(X[0]) == 2:
        Z = [[], []]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    Z[i][j] += X[j][k] * Y[k][j]

        return Z


print MatrixMultiplication()
