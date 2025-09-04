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

    for match in re.finditer(r">([^<>]+)(?=<|$)",y):
        if match.group(0) == ">\n    " or ">\n  " == match.group(0):
            break
        tokens.append(('TAG_TEXTO',match.group(0)))

print(tokens)