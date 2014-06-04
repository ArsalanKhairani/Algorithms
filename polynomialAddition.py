################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                 Polynomial Addition and Multiplication                     ##
##                                                                            ##
## Add two same size polynomials vector. List comprehensions are used for     ##
## addition.                                                                  ##
################################################################################

# Function: Add two same sized polynomial vectors
# Example : [1, 4, 5, 2] + [0, 7, 3, 2] = [1, 11, 8, 4]
def polynomialAddition(p, q):
    return [p[i] + q[i] for i in range(len(p))]

# Function: Multiply two polynomial vectors
# Example : [5, 0, 2] * [7, 0, 2, 1] = [35, 0, 24, 5, 4, 2]
def polynomialMultiplication(p, q):
    mul = [0 for i in range(len(p) + len(q) - 1)]
    for i in range(len(p)):
        for j in range(len(q)):
            mul[i+j] += p[i]*q[j]

    return mul

print (polynomialAddition([1, 4, 5, 2], [0, 7, 3, 2]))
print (polynomialMultiplication([5, 0, 2], [7, 0, 2, 1]))
