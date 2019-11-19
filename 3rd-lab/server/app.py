# /api/data doesn't insert or update any data... select works ok..
from flask import Flask, request, render_template, render_template_string, g, current_app
import json
import socket
import sqlite3

app = Flask(__name__, static_url_path='/static')

HOST = '127.0.0.1'
PORT = 1337
DATABASE_PATH = "/home/t33/projects/python-labs/3rd-lab/server/info.db"
#conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
#cursor = conn.cursor()


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
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT server, data FROM data_table")
    rows = cur.fetchall()
    new_list = {}
    if not rows:
        return render_template('index.html', ip=None, data={})
    for row in rows:
#        temp_json = json.loads(var['data'])
        #print("=>: ", row['data'])
        #print("json: ", type(row['data']))
        print(row)
        #ip = row['server']
        ip = row[0]
        try:
            #json_l = json.loads(row['data'])
            json_l = json.loads(row[1])
        except:
            json_l = {'data' : 'Null'} 
        new_list[ip] = json_l
    conn.close()
    return render_template('index.html', ip=ip, data=new_list)


@app.route("/api/data", methods=["POST", "GET"])
def data_receive():
    # insert with sqlite3.connect(DBPATH) as conn:
    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()
    #curs = get_db().cursor()
    print(f"req.getjson: {request.get_json()}")
    post = json.dumps(request.get_json())
    ip = request.remote_addr
    print(f"[!] POST: {post} <=> HOST: {(ip)}")
    print(curs.description)
    curs.execute("""INSERT INTO data_table (`server`, `data`) VALUES (?, ?)""", (ip, post))
    conn.commit()
    conn.close()
    return "Heh"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
