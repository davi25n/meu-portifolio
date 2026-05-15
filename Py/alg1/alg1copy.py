def multiplos(a,b,c):
    contador = a
    while contador <= b:
        multiplos = 0
        while contador <= b and contador  % c ==0:
            multiplos += 1
            contador += c
        contador += 1
    return multiplos

print(multiplos(1,10,2))