################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                        Karatsuba Multiplication                            ##
##                                                                            ##
## Recursive Algorithm for multiplying two big integers.                      ##
################################################################################

# For ceil funciton
import math

# Function: Recursive function with base case when x and y are 1 digit number 
# Example : 1234 * 5678 = 7006652
def KaratsubaMultiplication (n, x, y):

    # Base Case
    if n == 1:
        return x*y
    
    # compute a, b, c, and d
    a = int(x / math.ceil(10**(n/2)))
    b = int(x - (a*10**(n/2)))
    c = int(y / math.ceil(10**(n/2)))
    d = int(y - (c*10**(n/2)))

    # step 1: compute A.C
    ac = KaratsubaMultiplication(n/2, a, c)

    # step 2: compute B.D
    bd =  KaratsubaMultiplication(n/2, b, d)

    # step 3: compute (A+B)(C+D)
    ab_cd = KaratsubaMultiplication(n/2, (a+b), (c+d))

    # step 4: computer ad + bc
    ad_bc = ab_cd - ac - bd

    # step 5: Add them
    product = int((ac * 10**n) + (ad_bc * 10**(n/2)) + bd)

    return product

print (KaratsubaMultiplication(4, 1234, 5678))
