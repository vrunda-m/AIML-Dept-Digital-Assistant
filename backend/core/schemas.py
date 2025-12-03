import sqlite3

# Connect (or create) database
conn = sqlite3.connect('academic.db')
c = conn.cursor()

# Create student table
c.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usn TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    batch TEXT,
    roll_no INTEGER
)
''')

# Create subjects table
c.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    subject_code TEXT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    semester INTEGER
)
''')

# Create marks table
c.execute('''
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_code TEXT NOT NULL,
    marks REAL,
    UNIQUE(student_id, subject_code),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (subject_code) REFERENCES subjects(subject_code)
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully!")
