import sqlite3

# Connect to the database
conn = sqlite3.connect('academic.db')
c = conn.cursor()

# Insert sample students
students = [
    ('20A13DCDMS', 'Alice', '20', 1),
    ('20A13DCDSA', 'Bob', '20', 2),
    ('20A13DCPYP', 'Charlie', '20', 3)
]

for usn, name, batch, roll_no in students:
    c.execute('INSERT OR IGNORE INTO student (usn, name, batch, roll_no) VALUES (?, ?, ?, ?)',
              (usn, name, batch, roll_no))

# Insert sample subjects
subjects = [
    ('20A13DCOPS', 'Operating Systems', 3),
    ('20A13CSWE', 'Software Engineering', 3),
    ('20MA31MMAT', 'Mathematics', 3)
]

for code, name, sem in subjects:
    c.execute('INSERT OR IGNORE INTO subjects (subject_code, subject_name, semester) VALUES (?, ?, ?)',
              (code, name, sem))

# Insert sample marks
marks = [
    (1, '20A13DCOPS', 85),
    (1, '20A13CSWE', 90),
    (1, '20MA31MMAT', 80),
    (2, '20A13DCOPS', 70),
    (2, '20A13CSWE', 75),
    (2, '20MA31MMAT', 85),
    (3, '20A13DCOPS', 60),
    (3, '20A13CSWE', 65),
    (3, '20MA31MMAT', 70)
]

for student_id, subject_code, mark in marks:
    c.execute('INSERT OR IGNORE INTO marks (student_id, subject_code, marks) VALUES (?, ?, ?)',
              (student_id, subject_code, mark))

conn.commit()
conn.close()

print("Sample data inserted successfully!")
