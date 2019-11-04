from flask import Flask, request

app = Flask(__name__)
@app.route("/kek")
def kek():
    name = request.args.get("name", "world")
    "
    return f"Hell0, {name}"
