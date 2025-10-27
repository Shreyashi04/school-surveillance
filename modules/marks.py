import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from styles.theme import *
from database import db_setup
import matplotlib.pyplot as plt

# ============================ TEACHER WINDOW ============================
def open_marks_window(parent, teacher_name):
    top = tk.Toplevel(parent)
    top.title("Give Marks")
    top.geometry("520x460")
    top.configure(bg=BG_COLOR)

    tk.Label(top, text=f"Teacher: {teacher_name}", bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 12)).pack(pady=8)
    tk.Label(top, text="Enter marks for student", bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 14, "bold")).pack(pady=8)

    entries = {}
    for label in ["Student Name", "Class", "Subject", "Marks"]:
        tk.Label(top, text=label, bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 11)).pack()
        e = tk.Entry(top, font=("Poppins", 11))
        e.pack(pady=4)
        entries[label] = e

    def save():
        try:
            name = entries["Student Name"].get().strip()
            class_ = entries["Class"].get().strip()
            subject = entries["Subject"].get().strip()
            marks = int(entries["Marks"].get().strip())
            if not (name and class_ and subject):
                raise ValueError("All fields are required.")
        except Exception as ex:
            messagebox.showerror("Error", f"Invalid input: {ex}")
            return
        
        # ✅ Record teacher name in marks
        db_setup.add_mark(name, class_, subject, marks, teacher_name)
        messagebox.showinfo("Saved", f"Marks recorded by {teacher_name}.")
        for e in entries.values():
            e.delete(0, tk.END)

    tk.Button(top, text="Save Marks", bg=ACCENT_COLOR, fg="white", font=BUTTON_FONT,
              width=18, command=save).pack(pady=12)
    
# def get_all_marks():
#     """Fetch all marks entries from the database."""
#     conn = sqlite3.connect("database/school.db")
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT s.name AS student_name, s.class AS student_class,
#                m.subject, m.marks, m.date, t.name AS teacher_name
#         FROM marks m
#         JOIN students s ON s.id = m.student_id
#         JOIN teachers t ON t.id = m.teacher_id
#         ORDER BY m.date DESC
#     """)
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# ============================ STUDENT VIEW ============================
def show_marks_for_student(parent, student_name):
    """Shows all marks with teacher info for a student."""
    top = tk.Toplevel(parent)
    top.title("My Marks")
    top.geometry("650x400")
    top.configure(bg=BG_COLOR)

    tk.Label(top, text=f"Marks of {student_name}", bg=BG_COLOR, fg=TEXT_COLOR,
             font=("Poppins", 16, "bold")).pack(pady=10)

    # Fetch data
    rows = db_setup.get_marks_for_student(student_name)
    if not rows:
        tk.Label(top, text="No marks data available.", bg=BG_COLOR, fg="gray",
                 font=("Poppins", 12)).pack(pady=20)
        return

    # Scrollable Treeview
    frame = tk.Frame(top, bg=BG_COLOR)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    cols = ("Date", "Subject", "Marks", "Teacher")
    tree = ttk.Treeview(frame, columns=cols, show="headings", height=10)
    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    # Style tree
    style = ttk.Style()
    style.configure("Treeview",
                    background=BG_COLOR,
                    fieldbackground=BG_COLOR,
                    foreground=TEXT_COLOR,
                    font=("Poppins", 10))
    style.configure("Treeview.Heading",
                    background=ACCENT_COLOR,
                    foreground="white",
                    font=("Poppins", 11, "bold"))

    # Insert data
    
    for r in rows:
        teacher = r["teacher_name"] if "teacher_name" in r.keys() else "—"
        tree.insert("", "end", values=(r["date"], r["subject"], r["marks"], teacher))

# ============================ GRAPH ============================
def show_performance_graph(student_name):
    """Plots marks bar chart for a student."""
    rows = db_setup.get_marks_for_student(student_name)
    if not rows:
        tk.messagebox.showinfo("Performance", "No marks data to plot.")
        return

    subjects = [r['subject'] for r in rows]
    marks = [r['marks'] for r in rows]

    plt.figure(figsize=(6, 4))
    plt.bar(subjects, marks, color="#4CAF50")
    plt.title(f"{student_name} - Performance")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()
