from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "secret_counter"


@app.route("/")
def index():
    if "secret_counter" not in session:
        session["secret_counter"] = 0
    session["secret_counter"] += 1
    print(session["secret_counter"])
    return render_template("index.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
