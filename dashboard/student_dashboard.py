# dashboard/student_dashboard.py
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
from styles.theme import *
from modules import marks as marks_mod
from modules import attendance as att_mod
from modules import profile as profile_mod


def open_student_dashboard(parent, student_name):
    """Opens the main dashboard for a student after login."""
    try:
        parent.destroy()
    except:
        pass

    root = tk.Tk()
    root.title(f"{student_name} - Student Dashboard")
    root.state("zoomed")

    root.configure(bg=BG_COLOR)

    # ===== HEADER =====
    header = tk.Frame(root, bg=HEADER_BG, height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏫 Student Dashboard",
        bg=HEADER_BG,
        fg=TEXT_COLOR,
        font=("Poppins", 20, "bold")
    ).place(x=20, y=25)

    tk.Label(
        header,
        text=f"Welcome, {student_name}",
        bg=HEADER_BG,
        fg=TEXT_COLOR,
        font=("Poppins", 12)
    ).place(x=500, y=30)

    # ===== MAIN BUTTON AREA =====
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=40)

    btn_cfg = {
        "bg": ACCENT_COLOR,
        "fg": "white",
        "font": BUTTON_FONT,
        "width": 22,
        "height": 2,
        "relief": "flat"
    }

    tk.Button(
        frame, text="📘 View Marks",
        command=lambda: view_marks(root, student_name),
        **btn_cfg
    ).grid(row=0, column=0, padx=20, pady=10)

    tk.Button(
        frame, text="📗 View Attendance",
        command=lambda: view_attendance(root, student_name),
        **btn_cfg
    ).grid(row=0, column=1, padx=20, pady=10)

    tk.Button(
        frame, text="📊 Performance Graph",
        command=lambda: marks_mod.show_performance_graph(student_name),
        **btn_cfg
    ).grid(row=1, column=0, padx=20, pady=10)

    tk.Button(
        frame, text="🧾 My Profile",
        command=lambda: profile_mod.open_student_profile(root, student_name),
        **btn_cfg
    ).grid(row=1, column=1, padx=20, pady=10)

    tk.Button(
        frame, text="🔙 Logout",
        command=lambda: logout(root),
        **btn_cfg
    ).grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()


# ✅ MARKS TABLE VIEW
def view_marks(parent, student_name):
    """Displays marks for the logged-in student in a table."""
    # rows = marks_mod.(student_name)
    rows = marks_mod.show_marks_for_student(parent, student_name)

    
    if  rows:
        # ===== WINDOW =====
        top = tk.Toplevel(parent)
        top.title("📘 Marks Record")
        top.geometry("600x400")
        top.configure(bg=BG_COLOR)

        tk.Label(top, text=f"Marks of {student_name}",
                font=("Poppins", 16, "bold"),
                bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        # ===== TABLE FRAME =====
        table_frame = tk.Frame(top, bg=BG_COLOR)
        table_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Scrollbars
        y_scroll = tk.Scrollbar(table_frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        # Treeview for table
        tree = ttk.Treeview(
            table_frame,
            columns=("date", "subject", "marks", "teacher"),
            show="headings",
            yscrollcommand=y_scroll.set,
            height=10
        )

        # Configure scrollbar
        y_scroll.config(command=tree.yview)

        # Define headings
        tree.heading("date", text="Date")
        tree.heading("subject", text="Subject")
        tree.heading("marks", text="Marks")
        tree.heading("teacher", text="Teacher")

        # Define column widths
        tree.column("date", width=100, anchor="center")
        tree.column("subject", width=180, anchor="center")
        tree.column("marks", width=100, anchor="center")
        tree.column("teacher", width=180, anchor="center")

        # Insert data
        for r in rows:
            teacher = r["teacher_name"] if "teacher_name" in r.keys() else "—"
            tree.insert("", "end", values=(r["date"], r["subject"], r["marks"], teacher))

        # Style Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#f5f5f5",
                        fieldbackground="#f5f5f5",
                        font=("Poppins", 10),
                        rowheight=28)
        style.configure("Treeview.Heading",
                        background=ACCENT_COLOR,
                        foreground="white",
                        font=("Poppins", 11, "bold"))

        tree.pack(fill="both", expand=True, padx=10, pady=5)

    # else:
    #     messagebox.showinfo("Marks", "No marks records found.")
    #     return
        

def view_attendance(parent, student_name):
    """Displays attendance for the logged-in student."""
    rows = att_mod.get_attendance_for_student(student_name)

    if not rows:
        messagebox.showinfo("Attendance", "No attendance records found.")
        return

    top = tk.Toplevel(parent)
    top.title("📗 Attendance Record")
    top.geometry("500x400")
    top.configure(bg=BG_COLOR)

    tk.Label(top, text=f"Attendance of {student_name}",
             font=("Poppins", 16, "bold"),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    table_frame = tk.Frame(top, bg=BG_COLOR)
    table_frame.pack(padx=20, pady=10, fill="both", expand=True)

    y_scroll = tk.Scrollbar(table_frame, orient="vertical")
    y_scroll.pack(side="right", fill="y")

    tree = ttk.Treeview(
        table_frame,
        columns=("date", "subject", "status"),
        show="headings",
        yscrollcommand=y_scroll.set,
        height=10
    )
    y_scroll.config(command=tree.yview)

    tree.heading("date", text="Date")
    tree.heading("subject", text="Subject")
    tree.heading("status", text="Status")

    tree.column("date", width=120, anchor="center")
    tree.column("subject", width=200, anchor="center")
    tree.column("status", width=120, anchor="center")

    for r in rows:
        tree.insert("", "end", values=(r["date"], r["subject"], r["status"]))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#f5f5f5",
                    fieldbackground="#f5f5f5",
                    font=("Poppins", 10),
                    rowheight=28)
    style.configure("Treeview.Heading",
                    background=ACCENT_COLOR,
                    foreground="white",
                    font=("Poppins", 11, "bold"))

    tree.pack(fill="both", expand=True, padx=10, pady=5)


def logout(root):
    """Logs out and returns to main.py"""
    if messagebox.askyesno("Logout", "Do you want to logout?"):
        root.destroy()
        try:
            subprocess.Popen(["python", "main.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not return to main menu.\n{e}")
