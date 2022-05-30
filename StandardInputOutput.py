# ====================== List/Array Copy ========================================
A = [1, 2, 3] 
B = A  # Never use it for copy
B = A[:] # use is for copy array

# ========================= Reverse array ======================================
B = A[::-1]

#========================= Reverse loop =======================================
for i in range(9, -1, -1):
    print(i) # include 9 and exclude -1 === [9-0]

# =========================  2D Matrix =======================================
# M = [[0] * 10] * 10 #  Do not write this
M1 = [[0]*10 for i in range(10)]
M2 = [[0 for i in range(10)] for i in range(10)]

# ======================== Standard input output ==================================
from random import randint
from sys import stdin

def readint():
    # return int(input())
    return int(stdin.readline())

def readarray(typ):
    # return list(map(typ, input().split()))
    return list(map(typ, stdin.readline().split()))

def readatrix(n):
    M = []
    
    for i in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)

    return M

def mult(M,v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0,1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C,x)

if __name__=='__main__':
    n = readint()
    A = readatrix(n) 
    B = readatrix(n) 
    C = readatrix(n) 
    
    print(freivalds(A, B, C))