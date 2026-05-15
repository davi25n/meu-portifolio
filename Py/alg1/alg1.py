def multiplosmatematico(a,b,c):
    intervalointeiro = a // c
    intervalo = b - intervalointeiro * c
    if a % c == 0:
        return (intervalo // c) + 1
    else:
        return intervalo // c

def multiplosmatematico2(a,b,c):
    return (b // c) - ((a - 1) // c)

def multiploswhile(a,b,c):
    multiplos = 0
    while a <= b:
        if a % c == 0:
            while a <= b:
                a += c
                multiplos += 1
                print(a)
        else:
            a += 1
    return multiplos

print(multiplosmatematico(45,6775567985,5))
print(multiplosmatematico2(45,6775567985,5))
print(multiploswhile(45,6775567985,5))