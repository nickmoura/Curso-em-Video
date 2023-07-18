from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def tinta():
    return render_template("tinta.html")

if __name__ == "__main__":
    app.run(debug=True)