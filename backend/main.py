from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI(title="🎓 Academic Chatbot Backend")

DB_PATH = "database/academic_chatbot.db"

# ------------------------------------------
# 🧠 Helper to run SQL and return DataFrame
# ------------------------------------------
def run_query(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


@app.get("/")
def home():
    return {"message": "🎓 Academic Chatbot Backend is running!"}


# ------------------------------------------
# 🧾 Get list of all students
# ------------------------------------------
@app.get("/students")
def get_students():
    df = run_query("SELECT usn, name, batch FROM student ORDER BY usn;")
    return df.to_dict(orient="records")


# ------------------------------------------
# 📊 Get full semester-wise results for a student
# ------------------------------------------
@app.get("/student/{usn}")
def get_student_results(usn: str):
    try:
        print(f"🔍 Fetching results for USN: {usn}")

        query = """
            SELECT s.usn, s.name, sub.subject_name, sub.semester, m.marks
            FROM marks m
            JOIN student s ON m.student_id = s.id
            JOIN subjects sub ON m.subject_code = sub.subject_code
            WHERE s.usn = ?;
        """
        df = run_query(query, (usn,))

        if df.empty:
            return {"error": f"No results found for USN {usn}"}

        df["marks"] = pd.to_numeric(df["marks"], errors="coerce").fillna(0)

        # 🧮 Group results semester-wise
        semesters = {}
        for sem, group in df.groupby("semester"):
            sem_avg = group["marks"].mean()
            sem_cgpa = round(sem_avg / 10, 2)
            semesters[sem] = {
                "cgpa": sem_cgpa,
                "subjects": [
                    {"subject": row["subject_name"], "marks": float(row["marks"])}
                    for _, row in group.iterrows()
                ]
            }

        # 🎯 Overall CGPA
        overall_cgpa = round(df["marks"].mean() / 10, 2)

        return {
            "usn": str(df["usn"][0]),
            "name": str(df["name"][0]),
            "semesters": semesters,
            "overall_cgpa": overall_cgpa
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


# ------------------------------------------
# 🥇 Class summary — average & topper
# ------------------------------------------
@app.get("/class-summary")
def class_summary():
    try:
        query = """
            SELECT s.name, s.usn, AVG(m.marks) AS avg_marks
            FROM marks m
            JOIN student s ON m.student_id = s.id
            GROUP BY s.id;
        """
        df = run_query(query)
        if df.empty:
            return {"error": "No data found."}

        topper = df.loc[df["avg_marks"].idxmax()]
        class_avg = df["avg_marks"].mean()

        return {
            "class_average": round(class_avg, 2),
            "topper_name": topper["name"],
            "topper_usn": topper["usn"],
            "topper_avg": round(topper["avg_marks"], 2)
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


