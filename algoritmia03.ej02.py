def convertString(s):
    numberStr=str(s)
    sol=""
    print(len(numberStr))
    for i in range(0,len(numberStr)):
        sol+=""+numberStr[i]
    return sol

print(convertString(30303))