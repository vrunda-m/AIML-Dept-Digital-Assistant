# backend/database/check_db.py
import sqlite3

conn = sqlite3.connect("database/academic_chatbot.db")
cur = conn.cursor()

print("✅ Showing first 5 students:\n")
for row in cur.execute("SELECT usn, name FROM student LIMIT 5;"):
    print(row)

conn.close()
