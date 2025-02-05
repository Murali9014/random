from flask import Flask, render_template, request
import random
import string

app = Flask(_name_)

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+[]{}|;:,.<>?"
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        password = generate_password(length)
    return render_template("index.html", password=password)

if _name_ == "_main_":
    app.run(debug=True)