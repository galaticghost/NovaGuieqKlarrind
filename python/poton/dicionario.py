def ler_dict():
    dicionario = set()
    with open("dicionario.txt",'r',encoding="utf-8") as linhas:
        for linha in linhas:
            dicionario.add(linha.strip().lower())
        return dicionario