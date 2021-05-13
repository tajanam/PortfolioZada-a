from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutme", methods=["GET"])
def aboutme():
    return render_template("aboutme.html")

@app.route("/contact", methods=["POST"])
def contact():






if __name__ == "__main__":
    app.run()