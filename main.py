from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/add.html", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        success, message = dbHandler.insertContact(email, name)
        return render_template(
            "/add.html", is_done=True, error_message=None if success else message
        )
    else:
        return render_template("/add.html", error_message=None)


@app.route("/about.html", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        return render_template("/about.html", jit=True)
    else:
        return render_template("/about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
