def Lister(m, n, c):
    list=[]
    solve=""
    for e in range(0,n):
        solve=solve+str(c)
    print(solve)
    for i in range(0,m):
        list.append(solve)
    return list
print(Lister(4,5,2))