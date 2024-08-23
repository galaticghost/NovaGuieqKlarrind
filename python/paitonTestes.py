#!/opt/homebrew/bin/python3
# paisoejieje
# busca ingredientes

def busca(ingredientes, str):
    resposta = []

    for x in ingredientes:
        if str.lower() in x.lower():
            resposta.append(x)
    return resposta

ingredientes = ["Requeijão", "queijo MozArellA", "Queijo"]

print(busca(ingredientes,"queiJo"))
print(busca(ingredientes,"frango"))
