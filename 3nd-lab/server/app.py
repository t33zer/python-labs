from flask import Flask, request, render_template
import json

app = Flask(__name__)
@app.route("/")
def users():
    #name = request.args.get("name", "world")
    #with open("users.txt", "r") as f:
    #    raw_users = f.read(4096)

    #users_json = json.loads(raw_users)
    #

    #jinj = Template("users are: {% for user in users_json['users']%}<tr>{{user}}</tr><td>{{user}}</td>{% endfor %}")

    ##return f"Hell0, {name}\n{% for user in users_json['users']%}"
    return render_template("index.html", memes=["indeed", "Joe", "Candice"])

if __name__ == "__main__":
    app.run(debug=True)
