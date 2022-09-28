def primo(palabra):
    sol="El numero es un numero primo"
    for i in range (2,palabra):
        if palabra % i == 0:
            sol="El numero no es un numero primo"
            break
    return sol

print(primo(7))
