# Program for polynomial addition both with linked list and array 10:05 - 10:10
# Since python is already a dyanamically typed language linked list implementation is a waste

def polynomialAddition(p, q):
    return [p[i] + q[i] for i in range(len(p))]

def polynomialMultiplication(p, q):
    mul = [0 for i in range(len(p) + len(q) - 1)]
    for i in range(len(p)):
        for j in range(len(q)):
            mul[i+j] += p[i]*q[j]

    return mul

print (polynomialAddition([1, 4, 5, 2], [0, 7, 3, 2]))
print (polynomialMultiplication([5, 0, 2], [7, 0, 2, 1]))
