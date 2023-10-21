from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1ª pagina do site
# route -> maximianomoreira.pt/usuarios ou / contatos
# função -> o que quer exibir na pagina web
# Templates
@app.route("/")  # app é a variavél que se usa no flask
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)


# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)