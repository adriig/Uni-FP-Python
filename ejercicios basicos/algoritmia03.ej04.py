def Lister(lista):
    list=[]
    solves=[]
    for e in lista:
        for i in range(0,len(lista)):
            solves.append(e)
        list.append(solves)
        solves= []
    return list
print(Lister(["a","b","c"]))