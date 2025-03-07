import dicionario
mensagem_criptografada = "ÔZÜZ.QÓÇK#CÕ,RI#!Ó,ÕÓAÜÕB#Z#,ÃZC!#ÔZÜZ#;!,ÜÀ?ÜZÜ#Z#?ÜZÇ!#Ç!,Ü!AZ#,ÕÓAÀÓB!#Ç!BÇ#!ÇAB;ÕÇ#!#A!ÓÃZ#ÍBÀAÕ#ÇB,!ÇÇÕKK#" #string criptografada

lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z','.',',',';','!',
    '?','Á','Ã','À','Â','É','Ê','Í','Ó','Õ','Ô','Ú','Ü','Ç'] # lista em ordem

chave = 0 # Chave inicial

frases = []

dicionario_set = dicionario.ler_dict()

while chave < 44: # 44 loops
    frase = list(mensagem_criptografada) # Separa a frase em caracteres separados 
    pos=0 # pega a posição inicial
    for letra in frase:
        if letra == "#": # caso haja espaço
            letra = ' '
        else:
            index_descriptografado = lista.index(letra) - chave
            if index_descriptografado < 0:
                index_descriptografado += 44 # reseta
            letra = lista[index_descriptografado]
        frase[pos] = letra
        pos += 1
    frase = str(''.join(frase))
    frases.append(frase)
    chave += 1

chave = 0
counters = []

for frase in frases:
    palavras = frase.split()
    counter = 0
    for palavra in palavras:
        if palavra.lower() in dicionario_set:
             counter += 1
    if counters == [] or counters[1] < counter:
        counters = [chave,counter]
    chave += 1
print(counters)