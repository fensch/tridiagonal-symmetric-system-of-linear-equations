import numpy as np

####################### insert your data for main diagonal, upper/lower diagonal and right hand side of the equation into these numpy arrays
mainDiag  = np.array([1,2,3]).astype(float)
upperDiag = np.array([4,5]).astype(float)
RHS       = np.array([5,6,8]).astype(float)
#######################


# solving system of linear equations with tridiagonal symmetric matrix (a mainDiag, u upperDiag, b RHS)
def solve(a, u, b):
    k = b.size-1
    c = np.zeros(k+1)
    # produce upper triangle matrix
    for i in range(1,k+1):
        dummy  = u[i-1]/a[i-1]
        a[i]   = a[i] - u[i-1] * dummy
        b[i]   = b[i] - b[i-1] * dummy
    # "backwards substitution"
    c[k] = b[k]/a[k]
    for i in range(k-1,0-1,-1):
        c[i] = (b[i]-c[i+1]*u[i])/a[i]
    return c

c = solve(mainDiag, upperDiag, RHS)
print(c)
