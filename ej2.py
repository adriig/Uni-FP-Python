# Declaramos el método invertir que recibirá como parámetro una variable (arrayL) de tipo string y otras 2 variables que recogerán los 
# 2 carácteres con los que haremos las sustituciones, .
def invertir(arrayL, caracter1, caracter2):

    # Declaramos una variable res que será la solución que devolveremos de tipo String
    res=''

    # Declaramos un método con el que recorreremos arrayL letra por letra e iremos comprobando 
    for letra in arrayL:
        if letra==caracter1:
            res += caracter2
        else: 
            res+=letra
    return res

print(invertir("adsadsa","a","g"))
