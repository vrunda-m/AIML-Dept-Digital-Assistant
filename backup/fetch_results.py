import sqlite3

# Connect to the database
conn = sqlite3.connect('academic.db')
c = conn.cursor()

# Fetch student results
c.execute('''
SELECT s.name, s.usn, SUM(m.marks) as total, AVG(m.marks) as percentage
FROM student s
JOIN marks m ON s.id = m.student_id
GROUP BY s.id
''')

results = c.fetchall()

print("Student Results:\n")
print(f"{'Name':15} {'USN':12} {'Total':5} {'Percentage':10}")
print("-"*45)

for row in results:
    name, usn, total, percentage = row
    print(f"{name:15} {usn:12} {int(total):5} {percentage:.2f}%")

conn.close()
