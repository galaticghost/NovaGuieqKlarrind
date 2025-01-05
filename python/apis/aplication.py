from flask import Flask, request
import sqlite3

app = Flask(__name__)

class Database:

    def __init__(self):
        self.conexao = sqlite3.connect("bebidas.sqlite",check_same_thread=False)
        self.cursor = self.conexao.cursor()

database = Database()

@app.route('/')
def index():
    return "hi"

@app.route("/bebidas")
def get_bebidas():
    sql = 'SELECT nome,descricao FROM bebidas;'
    bebidas = database.cursor.execute(sql)
    bebidas = bebidas.fetchall()

    output = []

    for bebida in bebidas:
        x = {
            "nome":bebida[0],
            "descricao":bebida[1]
        }
        output.append(x)

    return {"bebidas":output}

@app.route("/bebidas/<id>")
def get_bebida(id):
    sql = 'SELECT nome,descricao FROM bebidas WHERE id = ?;'
    bebidas = database.cursor.execute(sql,(id,)).fetchone()
    return {"nome":bebidas[0],"descricao":bebidas[1]} if bebidas is not None else {"error":"not found"}

@app.route("/bebidas", methods=["POST"])
def add_bebida():
    sql = 'INSERT INTO bebidas(nome,descricao) VALUES (?,?);'
    database.cursor.execute(sql,(request.json["nome"],request.json["descricao"]))
    database.conexao.commit()
    return {"id":database.cursor.lastrowid}

@app.route("/bebidas/<id>", methods=["PUT"])
def update_bebida(id):
    if exists_row(id):
        return {"error":"not found"}

    sql = 'UPDATE bebidas SET nome = ?, descricao = ? WHERE id = ?'
    database.cursor.execute(sql,(request.json["nome"],request.json["descricao"],id))
    database.conexao.commit()
    return {"message":"200"}

@app.route("/bebidas/<id>", methods=["DELETE"])
def delete_bebida(id):
    if exists_row(id):
        return {"error":"not found"}
    
    sql = 'DELETE FROM bebidas WHERE id = ?;'
    database.cursor.execute(sql,(id,))
    database.conexao.commit()
    return {"message":"200"}

def exists_row(id):
    sql = 'SELECT 1 FROM bebidas WHERE id = ?'
    exists = database.cursor.execute(sql,(id,)).fetchone()
    if exists is None:
        return True
