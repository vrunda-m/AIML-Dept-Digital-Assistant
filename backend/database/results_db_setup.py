import sqlite3

# Create new database
conn = sqlite3.connect("database/results_analysis.db")
cursor = conn.cursor()

# --- Create students table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usn TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL
)
''')

# --- Create subjects table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    subject_code TEXT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    semester INTEGER
)
''')

# --- Create marks table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_code TEXT NOT NULL,
    marks REAL,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_code) REFERENCES subjects(subject_code)
)
''')

conn.commit()
conn.close()

print("✅ results_analysis.db created with tables: students, subjects, marks")
