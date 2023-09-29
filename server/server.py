import flask from Flask 
app = Flask(__name__)

@app.route("/ask")
def ask():
    return {"answers": ["majd", "raed", "oussema"]}
if __name__ =="__main__":
    app.run(debug=True)