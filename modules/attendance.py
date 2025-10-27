# modules/attendance.py
import tkinter as tk
from tkinter import messagebox
from styles.theme import *
from database import db_setup
from datetime import datetime

def open_attendance_window(parent, teacher_name):
    top = tk.Toplevel(parent)
    top.title("Take Attendance")
    top.geometry("520x420")
    top.configure(bg=BG_COLOR)

    tk.Label(top, text=f"{teacher_name} — Mark Attendance", bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 14, "bold")).pack(pady=10)

    entries = {}
    for label in ["Student Name", "Class", "Subject"]:
        tk.Label(top, text=label, bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 11)).pack()
        e = tk.Entry(top, font=("Poppins", 11))
        e.pack(pady=4)
        entries[label] = e

    status_var = tk.StringVar(value="Present")
    tk.Label(top, text="Status", bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 11)).pack(pady=(10,0))
    status_menu = tk.OptionMenu(top, status_var, "Present", "Absent")
    status_menu.config(width=12)
    status_menu.pack(pady=6)

    def save():
        try:
            name = entries["Student Name"].get().strip()
            class_ = entries["Class"].get().strip()
            subject = entries["Subject"].get().strip()
            status = status_var.get()
            if not (name and class_ and subject):
                raise ValueError("All fields required")
        except Exception as ex:
            messagebox.showerror("Error", f"{ex}")
            return
        db_setup.add_attendance(name, class_, subject, status)
        messagebox.showinfo("Saved", "Attendance saved.")
        for e in entries.values():
            e.delete(0, tk.END)

    tk.Button(top, text="Save Attendance", bg=ACCENT_COLOR, fg="white", font=BUTTON_FONT, width=18, command=save).pack(pady=12)

# Student view utilities
def get_attendance_for_student(student_name):
    rows = db_setup.get_attendance_for_student(student_name)
    return rows

def get_attendance_summary(class_=None):
    return db_setup.get_attendance_summary(class_)
