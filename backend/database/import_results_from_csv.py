import os
import re
import pandas as pd
import sqlite3

# ==============================
# 🎓 Base Paths
# ==============================
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "academic_chatbot.db")

# ==============================
# 🧩 Detect Semester Automatically
# ==============================
def detect_semester(filename: str) -> int:
    """
    Detect semester number from file name (e.g., '4thsem.csv' -> 4)
    If filename is 'results.csv', default to semester 3.
    """
    if filename.lower().startswith("results"):
        print("📘 Detected 'results.csv' → Semester 3")
        return 3

    match = re.search(r"(\d+)", filename)
    if match:
        sem = int(match.group(1))
        print(f"🧮 Detected Semester: {sem}")
        return sem
    print("⚠️ Could not detect semester from file name — defaulting to 3")
    return 3

# ==============================
# 📥 Import Function
# ==============================
def import_results(csv_filename: str):
    CSV_PATH = os.path.join(BASE_DIR, csv_filename)
    SEMESTER = detect_semester(csv_filename)

    if not os.path.exists(CSV_PATH):
        print(f"❌ File not found: {CSV_PATH}")
        return

    print(f"\n📂 Reading CSV file: {CSV_PATH}")

    # --- Try multiple encodings to avoid decoding errors ---
    encodings_to_try = ["utf-8-sig", "utf-16", "ISO-8859-1", "latin1"]
    for enc in encodings_to_try:
        try:
            df = pd.read_csv(CSV_PATH, encoding=enc)
            print(f"✅ Successfully read CSV using encoding: {enc}")
            break
        except Exception as e:
            print(f"⚠️ Failed with {enc}: {e}")
    else:
        print("❌ Could not decode CSV with common encodings.")
        return

    print(f"✅ Columns detected: {list(df.columns)}")

    # --- Normalize columns ---
    df.columns = [c.strip().lower() for c in df.columns]

    # Identify USN and Name columns
    usn_col = next((c for c in df.columns if "usn" in c), None)
    name_col = next((c for c in df.columns if "name" in c), None)

    if not usn_col or not name_col:
        print("❌ Could not find 'USN' or 'Name' columns in CSV.")
        return

    # Filter subject columns (ignore metadata)
    subject_cols = [
        c for c in df.columns
        if c not in [usn_col, name_col, 'sl.no', 'grand total', 'percentage']
        and not c.startswith('unnamed')
    ]
    print(f"📘 Found subject columns: {subject_cols}")

    # --- Connect to DB ---
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # --- Insert subjects ---
    for subject_code in subject_cols:
        cur.execute("""
            INSERT OR IGNORE INTO subjects (subject_code, subject_name, semester)
            VALUES (?, ?, ?)
        """, (subject_code.upper(), subject_code.upper(), SEMESTER))

    # --- Insert students and marks ---
    for _, row in df.iterrows():
        usn = str(row[usn_col]).strip()
        name = str(row[name_col]).strip()
        if not usn or not name:
            continue

        # Insert student
        cur.execute("""
            INSERT OR IGNORE INTO student (usn, name, batch)
            VALUES (?, ?, ?)
        """, (usn, name, "2020"))

        cur.execute("SELECT id FROM student WHERE usn = ?", (usn,))
        student_id = cur.fetchone()[0]

        # Insert marks for each subject
        for subject_code in subject_cols:
            try:
                marks = float(row[subject_code])
            except (ValueError, TypeError):
                marks = None
            cur.execute("""
                INSERT OR REPLACE INTO marks (student_id, subject_code, marks)
                VALUES (?, ?, ?)
            """, (student_id, subject_code.upper(), marks))

    conn.commit()
    conn.close()
    print(f"✅ Semester {SEMESTER} results imported successfully!\n")

# ==============================
# 🚀 Run for All CSV Files
# ==============================
if __name__ == "__main__":
    print("📊 Starting Multi-Semester Import...")
    files = [
        "results.csv",  # 3rd sem
        "4thsem.csv",   # 4th sem
        "5thsem.csv",   # 5th sem
        "6thsem.csv"    # 6th sem
    ]

    for f in files:
        if os.path.exists(os.path.join(BASE_DIR, f)):
            import_results(f)
        else:
            print(f"⚠️ Skipping missing file: {f}")

    print("✅ All available CSV files imported successfully!")



