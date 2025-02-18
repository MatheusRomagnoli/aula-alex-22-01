from flask import Flask, render_template, request, redirect, request
import random
from data import lista_configuracao as listas

app = Flask(__name__)

# AQUI IRÁ TODAS AS MINHAS ROTAS
@app.route("/", methods=["GET"])
def pagina_inicial():
    cor_de_fundo = random.choice(listas.lista_cores)
    frase = random.choice(listas.lista_frases)
    return  render_template("inicial.html",
                            cor_de_fundo_html = cor_de_fundo,
                            frase_html = frase )


@app.route("/sobre")
def pagina_sobre():
    cor_de_fundo = random.choice(listas.lista_cores)
    return  render_template("sobre.html",
                            cor_de_fundo_html = cor_de_fundo)

@app.route("/cadastro", methods=["GET"])
def pagina_cadastro():
    cor_de_fundo = random.choice(listas.lista_cores)
    return  render_template("cadastro.html",
                            lista_frases_html = listas.lista_frases)
    

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarfrase():
    frase_vinda_do_html = request.form.get("frase")
    listas.lista_frases.append(frase_vinda_do_html)
    return redirect("/cadastro")

@app.route("/cores", methods=["GET"])
def pagina_cores():
    return render_template("cores.html", lista_cores_html=listas.lista_cores)

@app.route("/cadastrarcores", methods=["POST"])
def pagina_cadastrar_cores():
    cor = request.form.get("cor")
    listas.lista_cores.append(cor)
    return redirect("/cores")

@app.route("/cores/delete/<indice_cor>")
def delete_cores(indice_cor):
    # converte o índice pra numero inteiro (ele vem como string)
    indice_cor = int(indice_cor)
    # exclui a cor da lista pelo índice
    listas.lista_cores.pop(indice_cor)
    # redireciona para a pagina/rota /cores
    return redirect("/cores")


app.run(debug=True, host="0.0.0.0", port=8080)
