# /api/data doesn't insert or update any data... select works ok..
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


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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
    for row in rows:
#        temp_json = json.loads(var['data'])
        print("=>: ", row['data'])
        print("json: ", type(row['data']))
        ip = row['server']
        try:
            json_l = json.loads(row['data'])
        except:
            json_l = {'data' : 'Null'} 
        new_list[ip] = json_l
    ip = request.remote_addr
    return render_template('index.html', ip=ip, data=new_list)


@app.route("/api/data", methods=["POST", "GET"])
def data_receive():
    curs = get_db().cursor()
    post = json.dumps(request.get_json())
    ip = request.remote_addr
    print(f"[!] POST: {post} <=> HOST: {type(ip)}")
    print(curs.description)
    result = curs.execute("""INSERT INTO data_table (`server`, `data`) VALUES ('192.168.0.103', '{"json": "iscool"')""")
    # result = curs.execute("UPDATE data_table SET `server`='1337.1337.1337' WHERE id > 2")
    print(result)
    return "Heh"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
