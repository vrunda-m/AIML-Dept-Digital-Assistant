from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_results():
    conn = sqlite3.connect('academic.db')
    c = conn.cursor()
    c.execute('''
        SELECT s.name, s.usn, SUM(m.marks) as total, AVG(m.marks) as percentage
        FROM student s
        JOIN marks m ON s.id = m.student_id
        GROUP BY s.id
    ''')
    results = c.fetchall()
    conn.close()
    return [
        {"name": r[0], "usn": r[1], "total": r[2], "percentage": round(r[3], 2)}
        for r in results
    ]

@app.route('/api/results', methods=['GET'])
def results():
    return jsonify(get_results())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
