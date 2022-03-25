def bigMod(a,b,M):
    if b==0:
        return 1 % M
    x = bigMod(a, b//2, M)
    x = (x*x) % M
    if b%2==1:
        x = (x * a) % M
    return x

while True:
  try:
    a = int(input())
    b = int(input())
    M = int(input())
    
    # a,b,M = map(int, input().split())
    
    print(bigMod(a,b,M))
    input()
  except(EOFError):
    break


