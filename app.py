from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de cores para alterar o fundo do site
lista_cores = ["#FACADA",
               "#BABACA",
               "#9CFFAF",
               "E2ED98"]

# Lista de frases para a pagina inicial
lista_frases = ["Transforme suas ideias em sons. DAWs: a chave para a criatividade musical.",
                "Cada batida, cada melodia. Domine a arte da produção musical com DAWs.",
                "A música começa aqui. Descubra o poder das DAWs.",
                "Inspire-se, componha e edite. As DAWs tornam a produção musical acessível."]

# AQUI IRÁ TODAS AS MINHAS ROTAS
@app.route("/")
def pagina_inicial():
    cor_de_fundo = random.choice(lista_cores)
    frase = random.choice(lista_frases)
    return  render_template("inicial.html",
                            cor_de_fundo_html = cor_de_fundo,
                            frase_html = frase )


@app.route("/sobre")
def pagina_sobre():
    cor_de_fundo = random.choice(lista_cores)
    return  render_template("sobre.html",
                            cor_de_fundo_html = cor_de_fundo)

@app.route("/cadastro")
def pagina_cadastro():
    cor_de_fundo = random.choice(lista_cores)
    return  render_template("cadastro.html", lista_frases_html = lista_frases)
    

app.run(debug=True, host="0.0.0.0", port=8080)
