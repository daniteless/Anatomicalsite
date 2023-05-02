from flask import Flask, render_template

app = Flask(__name__)
# route -> anatomicalinterpreter.com/""
# função -> o que vc vai exibir na página
# templates

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# site no ar
if __name__ == "__main__":
    app.run(debug=True)