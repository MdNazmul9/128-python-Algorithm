# list = [2, 4, 3, 6, 8]
# list = [3, 5, 9, 7, 1, 3]

i = 0
dupe = False
cnt = 0
while i < len(list)-1:
    if (list[i] + list[i+1]) %2 != 0:
        del list[i+1]
        cnt+=1
        dupe = True
    elif dupe:
        del list[i]
        dupe = False
    else:
        i += 1
        
print(cnt)