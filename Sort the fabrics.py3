t = int(input())

for tc in range(t):
    n = int(input())
    colors = []
    d = []
    for i in range(n):
        c,di,ui = input().split()
        colors.append([c,ui])
        d.append([di,ui])
    
    colors.sort(key=lambda x:(x[0],x[1]))
    d.sort(key=lambda x:(x[0],x[1]))
    
    ans = 0
    for i in range(n):
        if colors[i][1] == d[i][1]:
            ans += 1
    print(f'Case #{tc+1}: {ans}')
