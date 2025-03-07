def ler_dict():
    dicionario = {}
    with open("dicionario.txt",'r',encoding="utf-8") as linhas:
        for linha in linhas:
            dicionario.app(linha.lower())
        return dicionario