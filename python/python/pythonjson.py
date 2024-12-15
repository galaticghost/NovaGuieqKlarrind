import json

x = {
    'cadu':'xina',
    'bola':4
}
with open("bola.json", "w") as bola:
    json.dump(x,bola)