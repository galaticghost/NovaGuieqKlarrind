mensagem1 = input("Digite a mensagem: ")

while True:
    try: 
        chave = int(input("Digite o número da chave: "))
        break
    except:
        print("A chave deve ser um número")

lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z','.',',',';','!',
    '?','Á','Ã','À','Â','É','Ê','Í','Ó','Õ','Ô','Ú','Ü','Ç']

mensagem = list(mensagem1)

pos = 0

for letra in mensagem:
    if letra == ' ':
        letra = '#'
    else:
        index_letra = lista.index(letra)
        index_criptografado = index_letra + chave
        if index_criptografado > 44:
            index_criptografado -= 44
        letra = lista[index_criptografado]
    mensagem[pos] = letra
    pos += 1

print(''.join(mensagem))