import re


TAGS = ['documento','titulo','corpo','paragrafo']

tokens = []

with open("texto.txt","r") as f:
    y = f.read()

    for match in re.finditer(r"<\w+>",y):
        tokens.append(('TAG_ABERTURA',match.group(0)))
        print(match.group(0))

    for match in re.finditer(r"</\w+>",y):
        tokens.append(('TAG_FECHA',match.group(0)))
        print(match.group(0))

    for match in re.finditer(r">\s*([^<>]+)(?=<|$)",y):
        tokens.append(('TAG_TEXTO',match.group()))
    
print(tokens)