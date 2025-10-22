# backend/database/db_setup.py
import sqlite3
import os

# Path for SQLite DB file
DB_PATH = "academic_chatbot.db"

# Create or connect
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# --- Create tables ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usn TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    batch TEXT,
    roll_no INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    subject_code TEXT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    semester INTEGER
)
''')

cursor.execute('''
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

# --- Sample data ---
students = [
    ('1DS20AI001', 'ABDUR RAHMAN', '2020', 1),
    ('1DS20AI002', 'ABHIJIT PATTANAIK', '2020', 2),
    ('1DS20AI003', 'ABHISHEK S A', '2020', 3)
]

subjects = [
    ('21AI61', 'Machine Learning', 6),
    ('21AI62', 'Artificial Intelligence', 6),
    ('21AI63', 'Big Data Analytics', 6)
]

marks = [
    (1, '21AI61', 88.5),
    (1, '21AI62', 91.0),
    (2, '21AI63', 79.0),
    (3, '21AI61', 85.0)
]

cursor.executemany("INSERT OR IGNORE INTO student (usn, name, batch, roll_no) VALUES (?, ?, ?, ?)", students)
cursor.executemany("INSERT OR IGNORE INTO subjects (subject_code, subject_name, semester) VALUES (?, ?, ?)", subjects)
cursor.executemany("INSERT OR IGNORE INTO marks (student_id, subject_code, marks) VALUES (?, ?, ?)", marks)

conn.commit()
conn.close()

print("✅ Database and tables created successfully with sample data.")
