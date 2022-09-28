def primo(palabra):
    sol=[]
    terminado=False
    i=1
    while terminado==False:
        i+=1
        num=True
        for e in range(2,i):
            if i % e == 0:
                num=False
        if num == True:
            sol.append(i)
        size=len(sol)
        if size==palabra:
            break
            terminado=True
    return sol

print(primo(4))
