from sys import stdin
for i in range(int(stdin.readline())):
    k = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    cnt = [0, 0]
    for a in arr:
        cnt [a & 1] +=1
    print(min(cnt))
    
    
        
    
            

        
            

        
