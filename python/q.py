lista = [1,2,3,4,5]

lista[0] = lista[0] * 2
lista[1] = lista[1] * 2
lista[2] = lista[2] * 2
lista[3] = lista[3] * 2
lista[4] = lista[4] * 2

print(lista)

if lista[0] % 2 == 1:
    lista.remove(lista[0])
if lista[1] % 2 == 1:
    lista.remove(lista[1])
if lista[2] % 2 == 1:
    lista.remove(lista[2])
if lista[3] % 2 == 1:
    lista.remove(lista[3])
if lista[4] % 2 == 1:
    lista.remove(lista[4])
print(lista)