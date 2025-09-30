import re

def tokenizer(file_name: str):
    tokens = []

    with open(file_name,"r") as f:
        y = f.read()

        for match in re.finditer(r"<\w+>",y):
            tokens.append(('TAG_ABERTURA',match.group(0)))

        for match in re.finditer(r"</\w+>",y):
            tokens.append(('TAG_FECHA',match.group(0)))

        for match in re.finditer(r">\s*([^<>]+)(?=<|$)",y):
            tokens.append(('TAG_TEXTO',match.group()))
    return tokens

print(tokenizer("texto.txt"))