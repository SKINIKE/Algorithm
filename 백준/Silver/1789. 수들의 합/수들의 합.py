s = int(input())
sn = 0
n = 0

while sn <= s:
    sn += n  
    if sn <= s: 
        n += 1 
    else:
        print(n - 1)