import re

def tokenizer(content):
    tokens = []
    pattern = re.compile(r"<\w+>|</\w+>|[^<>]+")

    tag_aberta = re.compile(r"<\w+>")
    tag_fecha = re.compile(r"</\w+>")
    tag_texto = re.compile(r"[^<>]+")

    for match in pattern.finditer(content):
        token = match.group().strip()
        if tag_aberta.search(token):
            token = token.replace("<","")
            token = token.replace(">","")
            tokens.append(('TAG_ABERTURA',token))
        elif tag_fecha.search(token):
            token = token.replace("<","")
            token = token.replace(">","")
            token = token.replace("/","")
            tokens.append(('TAG_FECHA',token))
        elif tag_texto.search(token):
            tokens.append(('TAG_TEXTO',token))
    return tokens