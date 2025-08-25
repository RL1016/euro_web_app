from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/commemoratives")
def commemoratives():
    return render_template("commemoratives.html")

@app.route("/nationales")
def nationales():
    return render_template("nationales.html")

@app.route('/<pays>_ccs')
def page_pays_commemoratives(pays):
    return render_template(f'{pays}_ccs.html')
    
if __name__ == "__main__":
    app.run(debug=True)