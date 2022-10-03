t = int(input())
for tc in range(t):
    n = int(input())
    colors = []
    de= []
    for i in range(n):
        c,d,u = input().split()
        colors.append([c,u])
        de.append([d,u])
    colors.sort(key=lambda x:(x[0],x[1]))
    de.sort(key=lambda x:(x[0],x[1]))
    ans = 0
    for i in range(n):
        if colors[i][1] == de[i][1]:
            ans += 1
    print('Case #'+str(tc+1)+': '+str(ans))
