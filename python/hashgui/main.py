import tkinter as tk
from hashlib import sha256

root = tk.Tk()

root.title("Hash")
root.geometry("350x250")

data = tk.Entry(root,width=10)
data.grid(column=1,row=0)
data_lbl = tk.Label(root,text="Data:")
data_lbl.grid(column=0,row=0)

rementente = tk.Entry(root,width=40)
rementente.grid(column=1,row=3)
rementente_lbl = tk.Label(root,text="Remetente")
rementente_lbl.grid(column=0,row=3)


destinatario = tk.Entry(root,width=40)
destinatario.grid(column=1,row=5)
destinatario_lbl = tk.Label(root,text="Destinatário")
destinatario_lbl.grid(column=0,row=5)

descricao = tk.Entry(root,width=100)
descricao.grid(column=1,row=7)
descricao_lbl = tk.Label(root,text="Descrição")
descricao_lbl.grid(column=0,row=7)

valor = tk.Entry(root,width=15)
valor.grid(column=1,row=9)
valor_lbl = tk.Label(root,text="Valor")
valor_lbl.grid(column=0,row=9)

hash_anterior = " "
linha = 0

def clicked():
    global hash_anterior,linha
    x = tk.Label(root, text="")
    x['text'] = sha256(data.get().encode('utf-8') +
                       rementente.get().encode('utf-8') +
                       destinatario.get().encode('utf-8') +
                       descricao.get().encode('utf-8') +
                       valor.get().encode('utf-8') +
                       hash_anterior.encode()).hexdigest()
    x.grid(column=2,row=linha)
    linha += 1
    hash_anterior = x['text']

btn = tk.Button(root, text="Clica-me",command=clicked)
btn.grid(column=1,row=11)

root.mainloop()
