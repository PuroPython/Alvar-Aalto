from flask import Flask, request

app = Flask(__name__)

@app.route("/tulos")
def nayta_tulos():
    tuolit = request.args.get("tuolit")
    try: return tuolit
    except: return "Jotain muuta"

@app.route("/pöytä")
def poyta():
    return "Pöytiä"

@app.route("/")
def hello_world():
    return """
        <img align=right src="/static/png-clipart-vitra-design-museum-artek-chair-furniture-armchair-angle-couch-thumbnail.png">
        <h1>Tervetuloa</h1>
        <form action="/tulos"enctype="application/x-www-urlencoded">
        Haku: <input name=tuolit type=text> 
        <input type=submit value="Hae">
        </form>
"""


if __name__ == "__main__":
    app.run(debug=True)