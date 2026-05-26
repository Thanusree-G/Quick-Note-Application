from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database
conn = sqlite3.connect('notes.db')
conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, note TEXT)')
conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect('notes.db')
    
    if request.method == 'POST':
        note = request.form['note']
        conn.execute('INSERT INTO notes (note) VALUES (?)', (note,))
        conn.commit()

    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()

    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)