from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3 as sq3

app = Flask(__name__)

# Create DB
def init_db():
    with sq3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ''')
init_db()

# Home
@app.route('/')  # ✅ Add route decorator here
def index():
    with sq3.connect('database.db') as conn:
        conn.row_factory = sq3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests ORDER BY timestamp DESC")
        rows = cur.fetchall()
    return render_template('index.html', requests=rows)

# Add request (from HTML form with method="POST")
@app.route('/add', methods=['POST'])
def add_request():
    name = request.form['name']
    rtype = request.form['type']
    location = request.form['location']
    description = request.form['description']

    with sq3.connect('database.db') as conn:
        conn.execute('''
            INSERT INTO requests (name, type, location, description)
            VALUES (?, ?, ?, ?)
        ''', (name, rtype, location, description))
    
    # ✅ Redirect back to homepage (auto reload)
    return redirect(url_for('index'))

# Get all requests (API mode - optional)
@app.route('/get')
def get_requests():
    with sq3.connect('database.db') as conn:
        conn.row_factory = sq3.Row
        cur = conn.execute('SELECT * FROM requests')
        rows = [dict(row) for row in cur.fetchall()]
    return jsonify(rows)

# Delete a request
@app.route('/delete/<int:rid>', methods=['DELETE'])
def delete_request(rid):
    with sq3.connect('database.db') as conn:
        conn.execute('DELETE FROM requests WHERE id = ?', (rid,))
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True)
