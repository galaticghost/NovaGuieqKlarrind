# paiton! (e agr o vim tem corzinha)
import os
if os.path.isdir("poton"):
    print("Já existe uma pasta poton, então não execute esse script denovo! carlinista")
else:
    os.mkdir("poton")
    print("Pasta \"Poton\" criada")