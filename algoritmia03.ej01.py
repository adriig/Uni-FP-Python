# Tenemos que convertir una variable tipo string a tipo int sin usar el método int(x)

# Lo podemos hacer de dos maneras

# La primera manera es usando el método ord(x) el cual nos permite pasar un valor cual sea a su valor "unario"
def convertInt(s):
    number=0
    for c in s:
        number=number*10 + ord(c) - ord('0')

    return number

# Este segundo método crearemos un diccionario en el que para cada número en formato string le asignaremos su número en formato int
def convertInt2(s):
    numbers=({"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9})
    sol=0
    for i in range(0,len(s)):
        if s[i].isnumeric():
            sol=sol*10+numbers[s[i]]
    return sol

print(convertInt2("3434"))