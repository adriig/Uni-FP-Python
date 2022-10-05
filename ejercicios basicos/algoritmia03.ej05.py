def Lister(lista):
    sol=""
    i=0
    word=""
    for e in lista:
        if e != " ":
            word=word+e
            i+=1
        if e == " ":
            i=0
            word=""
        if(len(word)>len(sol)):
            sol=word
    return sol
print(Lister("43 afdsf micak04'2'3"))