precos = [1.50,2.53,2.2,0.23]

IMPOSTO = .05

preco_final = list(map(lambda precos: precos * (1 +IMPOSTO),precos))

print(preco_final)


num = [43.02,32,0.5]
pot = [3,4,5]

xina = list(map(lambda numeros,pot: pow(numeros,pot),num,pot))

print(xina)