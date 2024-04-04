from flask import Flask, request, jsonify
from BancoDeDados import *

app = Flask(__name__)

@app.route("/")
def index():
    return ""
# --------- PRODUTOS --------- #
@app.get("/produtos")
def produtos():
    dados = request.get_json()
    if dados != {}:
        id = dados['id']
        return (jsonify(requisicaoGetPorId("produtos", id)),200)
    else:
        return (jsonify(requisicaoGet("produtos")),200) 


@app.post("/produtos")
def enviarProdutos():
    dados = request.get_json()
    nome = dados['nome']
    return(jsonify(requisicaoPost("produtos",nome)),201)
# --------- FIM PRODUTOS --------- #


# --------- USUARIOS --------- #
@app.get("/usuarios")
def usuarios():
    dados = request.get_json()
    if dados != {}:
        id = dados['id']
        return (jsonify(requisicaoGetPorId("usuarios", id)),200)
    else:
        return (jsonify(requisicaoGet("usuarios")),200) 

@app.post("/usuarios")
def enviarUsuarios():
    dados = request.get_json()
    nome = dados['nome']
    return(jsonify(requisicaoPost("usuarios",nome)),201)
# --------- FIM USUARIOS --------- #

# --------- SETORES --------- #
@app.get("/setores")
def setores():
    dados = request.get_json()
    if dados != {}:
        id = dados['id']
        return (jsonify(requisicaoGetPorId("setores", id)),200)
    else:
        return (jsonify(requisicaoGet("setores")),200) 

@app.post("/setores")
def enviarSetores():
    dados = request.get_json()
    nome = dados['nome']
    return(jsonify(requisicaoPost("setores",nome)),201)
# --------- FIM SETORES --------- #

# --------- CATEGORIAS --------- #
@app.get("/categorias")
def categorias():
    dados = request.get_json()
    if dados != {}:
        id = dados['id']
        return (jsonify(requisicaoGetPorId("categorias", id)),200)
    else:
        return (jsonify(requisicaoGet("categorias")),200) 
    

@app.post("/categorias")
def enviarCategorias():
    dados = request.get_json()
    nome = dados['nome']
    return(jsonify(requisicaoPost("categorias",nome)),201)
# --------- FIM CATEGORIAS --------- #