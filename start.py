 
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('eingabe.db')
    return conn


def db(c, conn):
    c.execute("select * from Eingaben")
    helper = c.fetchall()[-1][0]
    conn.commit()
    conn.close()
    return render_template("start.html", input=helper)

def liste(c):
    s = ""
    for row in c:
        s = s + row[0] + "\n"
    l = s.split('\n')
    return l

@app.route('/', methods=["GET", "POST"])
def start():
    get_db_connection()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Eingaben(eingabe TEXT)''')
    if request.method == "POST":
        eing = request.form.get('input')
        print(eing)
        if not eing:
            return("Inhalt benötigt!")
        else:
            c.execute('INSERT INTO Eingaben VALUES (?)', [eing])
            return db(c, conn)
        
    elif request.method == "GET":
        return db(c, conn)

@app.route('/Liste', methods=["GET", "POST"])
def showall():
    get_db_connection()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("select * from Eingaben")
    l = liste(c)
    return render_template("liste.html", Eingaben=l)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')


