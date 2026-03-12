from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# simple login credentials
USERNAME = "dice_admin"
PASSWORD = "dice12345"


@app.route("/")
def index():
    if "user" in session:
        return render_template("index.html")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username_login")
        password = request.form.get("password_login")

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect("/")

        return "Invalid username or password"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)