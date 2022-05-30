# INTEST - Enormous-Input -Test
from sys import stdin
# n, k = map(int, input().split())
n, k = map(int, stdin.readline().split())
cnt = 0
for i in range(n):
    # x = int(input())
    x = int(stdin.readline())
    if x% k == 0:
        cnt+=1
print(cnt)