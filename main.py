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
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_msg = request.form.get("contact-msg")

    print(contact_name)
    print(contact_email)
    print(contact_msg)

    return render_template("success.html")





if __name__ == "__main__":
    app.run()