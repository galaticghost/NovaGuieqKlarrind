valor_maior = 0
valor_menor = 0 
valor = 1
quantidade = 0
soma = 0

while valor > 0:
    valor = int(input("Digite um valor: "))

    if valor <= 0:
        break

    if valor_menor == 0:
        valor_menor = valor

    if valor > valor_maior:
        valor_maior = valor

    elif valor < valor_menor:
        valor_menor = valor

    quantidade += 1 # += é igual a quantidade == quantidade + 1

    soma += valor

print(f"O maior valor digitado foi {valor_maior}")
print(f"O menor valor digitado foi {valor_menor}")
print(f"A quantidade de valores inseridos foi de {quantidade}")
print(f"A soma dos valores é de {soma}")
print(f"A média dos valores é de {soma/quantidade}")