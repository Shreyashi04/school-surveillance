# # database/db_setup.py
# import sqlite3
# import os
# from datetime import datetime

# DB_PATH = os.path.join(os.path.dirname(__file__), "school.db")

# def get_conn():
#     os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# def init_db():
#     conn = get_conn()
#     cur = conn.cursor()
#     # Students
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             class TEXT NOT NULL,
#             roll TEXT,
#             password TEXT NOT NULL,
#             phone TEXT,
#             email TEXT
#         )
#     """)
#     # Teachers
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS teachers (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             subject TEXT,
#             password TEXT NOT NULL,
#             phone TEXT,
#             email TEXT
#         )
#     """)
#     # Marks
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS marks (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_name TEXT NOT NULL,
#             class TEXT,
#             subject TEXT,
#             marks INTEGER,
#             date TEXT
#         )
#     """)
#     # Attendance
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS attendance (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_name TEXT NOT NULL,
#             class TEXT,
#             subject TEXT,
#             date TEXT,
#             status TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# # Student helpers
# def add_student(name, class_, roll, password, phone=None, email=None):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO students (name, class, roll, password, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
#                 (name, class_, roll, password, phone, email))
#     conn.commit()
#     conn.close()

# def find_student(name, class_, password):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM students WHERE LOWER(name)=LOWER(?) AND class=? AND password=?", (name, class_, password))
#     row = cur.fetchone()
#     conn.close()
#     return row

# def get_student_profile(name):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM students WHERE LOWER(name)=LOWER(?)", (name,))
#     row = cur.fetchone()
#     conn.close()
#     return row

# def update_student_profile(student_id, name, class_, roll, password, phone, email):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("""UPDATE students SET name=?, class=?, roll=?, password=?, phone=?, email=? WHERE id=?""",
#                 (name, class_, roll, password, phone, email, student_id))
#     conn.commit()
#     conn.close()

# # Teacher helpers
# def add_teacher(name, subject, password, phone=None, email=None):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO teachers (name, subject, password, phone, email) VALUES (?, ?, ?, ?, ?)",
#                 (name, subject, password, phone, email))
#     conn.commit()
#     conn.close()

# def find_teacher(name, subject, password):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM teachers WHERE LOWER(name)=LOWER(?) AND LOWER(subject)=LOWER(?) AND password=?",
#                 (name, subject, password))
#     row = cur.fetchone()
#     conn.close()
#     return row

# def get_teacher_profile(name):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM teachers WHERE LOWER(name)=LOWER(?)", (name,))
#     row = cur.fetchone()
#     conn.close()
#     return row

# def update_teacher_profile(teacher_id, name, subject, password, phone, email):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("""UPDATE teachers SET name=?, subject=?, password=?, phone=?, email=? WHERE id=?""",
#                 (name, subject, password, phone, email, teacher_id))
#     conn.commit()
#     conn.close()

# # Marks helpers
# def add_mark(student_name, class_, subject, marks):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO marks (student_name, class, subject, marks, date) VALUES (?, ?, ?, ?, ?)",
#                 (student_name, class_, subject, marks, datetime.now().strftime("%Y-%m-%d")))
#     conn.commit()
#     conn.close()

# def get_marks_for_student(student_name):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM marks WHERE LOWER(student_name)=LOWER(?)", (student_name,))
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# def get_all_marks():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM marks ORDER BY date DESC")
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# # Attendance helpers
# def add_attendance(student_name, class_, subject, status, date=None):
#     conn = get_conn()
#     cur = conn.cursor()
#     if date is None:
#         date = datetime.now().strftime("%Y-%m-%d")
#     cur.execute("INSERT INTO attendance (student_name, class, subject, date, status) VALUES (?, ?, ?, ?, ?)",
#                 (student_name, class_, subject, date, status))
#     conn.commit()
#     conn.close()

# def get_attendance_for_student(student_name):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM attendance WHERE LOWER(student_name)=LOWER(?) ORDER BY date DESC", (student_name,))
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# def get_attendance_summary(class_=None):
#     conn = get_conn()
#     cur = conn.cursor()
#     if class_:
#         cur.execute("SELECT student_name, status, COUNT(*) as cnt FROM attendance WHERE class=? GROUP BY student_name, status", (class_,))
#     else:
#         cur.execute("SELECT student_name, status, COUNT(*) as cnt FROM attendance GROUP BY student_name, status")
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# # Initialize DB on import
# init_db()



import sqlite3
import os
from datetime import datetime

# ------------------------- CONFIG -------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "school.db")

# ------------------------- CONNECTION -------------------------
def get_conn():
    """Create SQLite connection with row access by column name."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ------------------------- INIT DATABASE -------------------------
def init_db():
    """Initialize database tables if not exist."""
    conn = get_conn()
    cur = conn.cursor()

    # Students
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            class TEXT NOT NULL,
            roll TEXT,
            password TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)

    # Teachers
    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT,
            password TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)

    # Marks
    cur.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            class TEXT,
            subject TEXT,
            marks INTEGER,
            teacher_name TEXT,
            date TEXT
        )
    """)

    # Attendance
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            class TEXT,
            subject TEXT,
            date TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

# ------------------------- ADD COLUMN SAFETY -------------------------
def add_teacher_name_column():
    """Ensure teacher_name column exists in marks table for backward compatibility."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(marks)")
    columns = [col[1] for col in cur.fetchall()]
    if "teacher_name" not in columns:
        cur.execute("ALTER TABLE marks ADD COLUMN teacher_name TEXT")
        conn.commit()
    conn.close()

# ------------------------- STUDENT HELPERS -------------------------
def add_student(name, class_, roll, password, phone=None, email=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (name, class, roll, password, phone, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, class_, roll, password, phone, email))
    conn.commit()
    conn.close()

def find_student(name, class_, password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM students
        WHERE LOWER(name)=LOWER(?) AND class=? AND password=?
    """, (name, class_, password))
    row = cur.fetchone()
    conn.close()
    return row

def get_student_profile(name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE LOWER(name)=LOWER(?)", (name,))
    row = cur.fetchone()
    conn.close()
    return row

def update_student_profile(student_id, name, class_, roll, password, phone, email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET name=?, class=?, roll=?, password=?, phone=?, email=?
        WHERE id=?
    """, (name, class_, roll, password, phone, email, student_id))
    conn.commit()
    conn.close()

# ------------------------- TEACHER HELPERS -------------------------
def add_teacher(name, subject, password, phone=None, email=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO teachers (name, subject, password, phone, email)
        VALUES (?, ?, ?, ?, ?)
    """, (name, subject, password, phone, email))
    conn.commit()
    conn.close()

def find_teacher(name, subject, password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM teachers
        WHERE LOWER(name)=LOWER(?) AND LOWER(subject)=LOWER(?) AND password=?
    """, (name, subject, password))
    row = cur.fetchone()
    conn.close()
    return row

def get_teacher_profile(name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers WHERE LOWER(name)=LOWER(?)", (name,))
    row = cur.fetchone()
    conn.close()
    return row

# # def get_teacher_profile(name, subject=None):
# #     """Fetch teacher profile by name (and subject if given)."""
# #     conn = get_conn()
# #     cur = conn.cursor()
# #     if subject:
# #         cur.execute("SELECT * FROM teachers WHERE LOWER(name)=LOWER(?) AND LOWER(subject)=LOWER(?)", (name, subject))
# #     else:
# #         cur.execute("SELECT * FROM teachers WHERE LOWER(name)=LOWER(?)", (name,))
# #     row = cur.fetchone()
# #     conn.close()
# #     return row

# def get_teacher_profile(name, subject=None):
#     conn = sqlite3.connect("school.db")
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()

#     if subject:
#         c.execute("SELECT * FROM teachers WHERE name=? AND subject=?", (name, subject))
#     else:
#         c.execute("SELECT * FROM teachers WHERE name=?", (name,))
    
#     row = c.fetchone()
#     conn.close()
#     return row

def update_teacher_profile(teacher_id, name, subject, password, phone, email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE teachers
        SET name=?, subject=?, password=?, phone=?, email=?
        WHERE id=?
    """, (name, subject, password, phone, email, teacher_id))
    conn.commit()
    conn.close()

# ------------------------- MARKS HELPERS -------------------------
def add_mark(student_name, class_, subject, marks, teacher_name=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO marks (student_name, class, subject, marks, teacher_name, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_name, class_, subject, marks, teacher_name, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def get_marks_for_student(student_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM marks
        WHERE LOWER(student_name)=LOWER(?)
        ORDER BY date DESC
    """, (student_name,))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_marks():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM marks ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_all_marks():
    """Delete all mark entries."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM marks")
    conn.commit()
    conn.close()

# ------------------------- ATTENDANCE HELPERS -------------------------
def add_attendance(student_name, class_, subject, status, date=None):
    conn = get_conn()
    cur = conn.cursor()
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    cur.execute("""
        INSERT INTO attendance (student_name, class, subject, date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (student_name, class_, subject, date, status))
    conn.commit()
    conn.close()

def get_attendance_for_student(student_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM attendance
        WHERE LOWER(student_name)=LOWER(?)
        ORDER BY date DESC
    """, (student_name,))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_attendance_summary(class_=None):
    conn = get_conn()
    cur = conn.cursor()
    if class_:
        cur.execute("""
            SELECT student_name, status, COUNT(*) as cnt
            FROM attendance
            WHERE class=?
            GROUP BY student_name, status
        """, (class_,))
    else:
        cur.execute("""
            SELECT student_name, status, COUNT(*) as cnt
            FROM attendance
            GROUP BY student_name, status
        """)
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_all_attendance():
    """Delete all attendance entries."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()

# ------------------------- INIT ON IMPORT -------------------------
init_db()
add_teacher_name_column()
