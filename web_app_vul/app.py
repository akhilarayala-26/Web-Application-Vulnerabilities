from flask import Flask, render_template, request, redirect, make_response, session
import sqlite3
from markupsafe import escape

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('webapp.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL);''')
    conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('login.html')

# Vulnerable SQL Injection Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('webapp.db')
    cursor = conn.cursor()
    
    # Vulnerable SQL query (SQL Injection)
    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user'] = user[1]
        return redirect('/success')
    else:
        return "Login Failed!"

# Success page
@app.route('/success')
def success():
    if 'user' in session:
        return render_template('success.html', username=session['user'])
    else:
        return redirect('/')

# XSS Vulnerable Page
@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        comment = request.form['comment']
        return render_template('xss.html', comment=comment)  # Vulnerable to XSS
    return render_template('xss.html', comment="")

# CSRF Vulnerability Demo
@app.route('/csrf', methods=['GET', 'POST'])
def csrf():
    if request.method == 'POST':
        return "CSRF attack successful!"
    return render_template('csrf.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
