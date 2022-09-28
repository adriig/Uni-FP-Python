def fact(numero):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo

print(fact(5232543465347554))

def primo(numero):
    primo=True
    i=2
    while primo == True and i < numero/2:
        if numero % i == 0:
            primo = False
        i+=1
    return primo

print(primo(37))


var=(4+1.0)
print(var)