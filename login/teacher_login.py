import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
from dashboard.teacher_dashboard import open_teacher_dashboard
from styles.theme import *

def open_teacher_login(parent=None):
    """Teacher Login Page - Fullscreen UI"""
    if parent:
        parent.destroy()

    root = tk.Tk()
    root.title("Teacher Login - Techno India Group Public School")
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
        tk.Label(header, text="[Logo Missing]", bg=HEADER_BG, fg=TEXT_COLOR, font=("Poppins", 16, "bold")).place(x=40, y=55)

    # School Name
    tk.Label(
        header,
        text="Techno India Group Public School",
        bg=HEADER_BG,
        fg=TEXT_COLOR,
        font=("Poppins", 28, "bold")
    ).place(x=200, y=40)

    # Portal subtitle
    tk.Label(
        header,
        text="Teacher Login Portal",
        bg=HEADER_BG,
        fg="#222222",
        font=("Poppins", 14, "italic")
    ).place(x=200, y=95)

    # ===== MAIN FORM AREA =====
    form_frame = tk.Frame(root, bg=BG_COLOR)
    form_frame.pack(expand=True)

    tk.Label(
        form_frame,
        text="👨‍🏫 Teacher Login",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Poppins", 26, "bold")
    ).pack(pady=20)

    entries = {}
    for field in ["Name", "Subject", "Password"]:
        tk.Label(
            form_frame, 
            text=field, 
            bg=BG_COLOR, 
            fg=TEXT_COLOR, 
            font=("Poppins", 14, "bold")
        ).pack(pady=(10, 5))
        entry = tk.Entry(
            form_frame, 
            font=("Poppins", 14), 
            width=30,
            show="*" if field == "Password" else ""
        )
        entry.pack(pady=5)
        entries[field] = entry

    def login():
        if all(e.get().strip() for e in entries.values()):
            open_teacher_dashboard(root, entries["Name"].get())
        else:
            messagebox.showerror("Error", "All fields are required!")

    # Buttons
    btn_frame = tk.Frame(form_frame, bg=BG_COLOR)
    btn_frame.pack(pady=30)

    tk.Button(
        btn_frame, text="Login", 
        bg=ACCENT_COLOR, fg="white",
        font=BUTTON_FONT, width=15, height=1,
        command=login
    ).grid(row=0, column=0, padx=20)

    tk.Button(
        btn_frame, text="🔙 Back", 
        bg="#555555", fg="white",
        font=BUTTON_FONT, width=15, height=1,
        command=lambda: back_to_main(root)
    ).grid(row=0, column=1, padx=20)

    root.mainloop()


def back_to_main(root):
    """Return to main.py"""
    root.destroy()
    try:
        subprocess.Popen(["python", "main.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open main page.\n{e}")
