import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import subprocess
import os
import sys
from styles.theme import *
from modules import marks as marks_mod
from modules import attendance as att_mod
from modules import profile as profile_mod


def open_teacher_dashboard(parent, teacher_name):
    """Main Teacher Dashboard UI"""
    try:
        parent.destroy()
    except:
        pass

    root = tk.Tk()
    root.title(f"{teacher_name} - Teacher Dashboard | Techno India Group Public School")
    root.state("zoomed")
    root.configure(bg=BG_COLOR)

    # ===== HEADER =====
    header = tk.Frame(root, bg=HEADER_BG, height=150)
    header.pack(fill="x")

    # Logo
    try:
        logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
        logo_path = os.path.abspath(logo_path)
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((120, 100), Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header, image=logo, bg=HEADER_BG)
        logo_label.image = logo
        logo_label.place(x=40, y=25)
    except Exception as e:
        print("⚠️ Logo Error:", e)
        tk.Label(
            header, text="[Logo Missing]", bg=HEADER_BG,
            fg=TEXT_COLOR, font=("Poppins", 16, "bold")
        ).place(x=40, y=55)

    # School Name + Subtitle
    tk.Label(
        header,
        text="Techno India Group Public School",
        bg=HEADER_BG, fg=TEXT_COLOR,
        font=("Poppins", 28, "bold")
    ).place(x=200, y=40)

    tk.Label(
        header,
        text=f"Teacher Dashboard — Welcome, {teacher_name}",
        bg=HEADER_BG, fg="#222222",
        font=("Poppins", 14, "italic")
    ).place(x=200, y=95)

    # ===== BUTTONS AREA =====
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(expand=True)

    btn_cfg = {
        "bg": ACCENT_COLOR,
        "fg": "white",
        "font": BUTTON_FONT,
        "width": 25,
        "height": 2,
        "relief": "flat"
    }

    # Buttons
    tk.Button(
        frame, text="🧮 Give Marks",
        command=lambda: marks_mod.open_marks_window(root, teacher_name),
        **btn_cfg
    ).grid(row=0, column=0, padx=25, pady=15)

    tk.Button(
        frame, text="🗓️ Take Attendance",
        command=lambda: att_mod.open_attendance_window(root, teacher_name),
        **btn_cfg
    ).grid(row=0, column=1, padx=25, pady=15)

    # tk.Button(
    #     frame, text="📊 View All Marks",
    #     command=lambda: show_all_marks(root),
    #     **btn_cfg
    # ).grid(row=1, column=0, padx=25, pady=15)

    tk.Button(
        frame, text="🧾 My Profile",
        command=lambda: profile_mod.open_teacher_profile(root, teacher_name),
        **btn_cfg
    ).grid(row=1, column=0, columnspan=2, padx=25, pady=15)


    # Logout button (separate color)
    tk.Button(
        frame, text="🔙 Logout",
        command=lambda: logout(root),
        bg="#444444", fg="white",
        font=BUTTON_FONT, width=25, height=2, relief="flat"
    ).grid(row=2, column=0, columnspan=2, pady=25)

    root.mainloop()


# # ===== SHOW ALL MARKS (TABLE FORMAT) =====
# def show_all_marks(parent):
#     """Display all marks in a fullscreen table."""
#     # Handle missing get_all_marks function
#     try:
#         rows = marks_mod.get_all_marks()
#     except AttributeError:
#         messagebox.showerror("Error", "⚠️ 'get_all_marks()' not found in marks module.")
#         return

#     if not rows:
#         messagebox.showinfo("Marks", "No marks recorded yet.")
#         return

#     top = tk.Toplevel(parent)
#     top.title("📊 All Student Marks")
#     top.state("zoomed")
#     top.configure(bg=BG_COLOR)

#     tk.Label(
#         top, text="All Students' Marks Records",
#         bg=BG_COLOR, fg=TEXT_COLOR,
#         font=("Poppins", 22, "bold")
#     ).pack(pady=20)

#     # Table Frame
#     table_frame = tk.Frame(top, bg=BG_COLOR)
#     table_frame.pack(padx=40, pady=10, fill="both", expand=True)

#     y_scroll = tk.Scrollbar(table_frame, orient="vertical")
#     y_scroll.pack(side="right", fill="y")

#     tree = ttk.Treeview(
#         table_frame,
#         columns=("student", "class", "subject", "marks", "date", "teacher"),
#         show="headings",
#         yscrollcommand=y_scroll.set
#     )
#     y_scroll.config(command=tree.yview)

#     # Headings
#     headings = {
#         "student": "Student Name",
#         "class": "Class",
#         "subject": "Subject",
#         "marks": "Marks",
#         "date": "Date",
#         "teacher": "Teacher"
#     }
#     for col, text in headings.items():
#         tree.heading(col, text=text)
#         tree.column(col, anchor="center", width=160 if col != "marks" else 100)

#     # Insert Data
#     for r in rows:
#         tree.insert("", "end", values=(
#             r.get("student_name", ""),
#             r.get("class", ""),
#             r.get("subject", ""),
#             r.get("marks", ""),
#             r.get("date", ""),
#             r.get("teacher_name", "")
#         ))

#     # Styling
#     style = ttk.Style()
#     style.theme_use("clam")
#     style.configure("Treeview",
#                     background="#f5f5f5",
#                     fieldbackground="#f5f5f5",
#                     font=("Poppins", 11),
#                     rowheight=30)
#     style.configure("Treeview.Heading",
#                     background=ACCENT_COLOR,
#                     foreground="white",
#                     font=("Poppins", 12, "bold"))

#     tree.pack(fill="both", expand=True, padx=10, pady=10)


def logout(root):
    """Logs out and returns to main.py"""
    if messagebox.askyesno("Logout", "Do you want to logout?"):
        root.destroy()
        try:
            subprocess.Popen([sys.executable, "main.py"])  # safer than "python"
        except Exception as e:
            messagebox.showerror("Error", f"Could not return to main menu.\n{e}")
