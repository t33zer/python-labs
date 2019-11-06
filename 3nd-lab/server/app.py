from flask import Flask, request, render_template, render_template_string, g, current_app
import json
import socket
import sqlite3

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = 1337
DATABASE_PATH = "/home/t33/projects/python-labs/3nd-lab/server/info.db"
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()


def init_db():
    db = get_db()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
        db.row_factory = sqlite3.Row
    return db
   # db = getattr(g, '_database', None)
   # if db is None:
   #     db = g._database = sqlite3.connect(DATABASE_PATH)

@app.route("/")
def index():
    #users_json = json.loads(raw_users)
    cur = get_db().cursor()
    cur.execute("SELECT server, data FROM data_table")
    rows = cur.fetchall()
    new_list = {}
    for var in rows:
#        temp_json = json.loads(var['data'])
        print("=>: ", var['data'])
        print("json: ", type(var['data']))
        ip = var['server']
        try:
            json_l = json.loads(var['data'])
        except:
            json_l = "NOT JSON"
        new_list[ip] = json_l
    return render_template('index.html', data=new_list)


if __name__ == "__main__":
    app.run(debug=True)
