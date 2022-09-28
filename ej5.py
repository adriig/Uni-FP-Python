def capicua(palabra):
    sol="Es capicua"
    texto=str(palabra)
    for i in range(0, len(texto)):
        print(texto[i])
        if texto[i]!=texto[len(texto)-i-1]:
            sol="No es capicua"
    return sol

print(capicua(43234))