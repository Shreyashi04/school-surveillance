# import tkinter as tk
# from tkinter import messagebox, PhotoImage
# from dashboard.student_dashboard import open_student_dashboard
# from styles.theme import *

# def open_student_login(prev_window):
#     # Close previous window (like main menu)
#     prev_window.destroy()

#     # Main window
#     root = tk.Tk()
#     root.title("Student Login - Techno India Group Public School")
#     root.state('zoomed')
#     root.configure(bg=BG_COLOR)

#     # ---------------- HEADER ----------------
#     header = tk.Frame(root, bg=ACCENT_COLOR, height=90)
#     header.pack(fill="x")

#     try:
#         logo = PhotoImage(file="assets/logo.png")  # <-- put your logo path here
#         logo_label = tk.Label(header, image=logo, bg=ACCENT_COLOR)
#         logo_label.image = logo
#         logo_label.pack(side="left", padx=20, pady=10)
#     except Exception:
#         logo_label = tk.Label(header, text="🏫", bg=ACCENT_COLOR, fg="white", font=("Poppins", 30))
#         logo_label.pack(side="left", padx=20, pady=10)

#     tk.Label(
#         header,
#         text="ABC Public School",
#         bg=ACCENT_COLOR,
#         fg="white",
#         font=("Poppins", 26, "bold")
#     ).pack(side="left", padx=10)

#     # Back button in header
#     def go_back():
#         root.destroy()
#         from main import open_main_page  # <- change this to your main file function
#         open_main_page()

#     tk.Button(
#         header,
#         text="← Back",
#         bg="white",
#         fg=ACCENT_COLOR,
#         font=("Poppins", 12, "bold"),
#         width=10,
#         command=go_back
#     ).pack(side="right", padx=20, pady=20)

#     # ---------------- LOGIN FORM ----------------
#     form_frame = tk.Frame(root, bg=BG_COLOR)
#     form_frame.pack(pady=80)

#     tk.Label(
#         form_frame,
#         text="Student Login Portal",
#         bg=BG_COLOR,
#         fg=TEXT_COLOR,
#         font=("Poppins", 22, "bold")
#     ).pack(pady=20)

#     entries = {}
#     fields = ["Name", "Roll No", "Class", "Password"]
#     for field in fields:
#         tk.Label(
#             form_frame,
#             text=field,
#             bg=BG_COLOR,
#             fg=TEXT_COLOR,
#             font=("Poppins", 14, "bold")
#         ).pack(pady=5)
#         entry = tk.Entry(
#             form_frame,
#             font=("Poppins", 13),
#             show="*" if field == "Password" else "",
#             width=28,
#             justify="center",
#             relief="solid",
#             bd=1
#         )
#         entry.pack(pady=6)
#         entries[field] = entry

#     # ---------------- LOGIN BUTTON ----------------
#     def login():
#         name = entries["Name"].get().strip()
#         roll = entries["Roll No"].get().strip()
#         class_ = entries["Class"].get().strip()
#         password = entries["Password"].get().strip()

#         if not all([name, roll, class_, password]):
#             messagebox.showerror("Error", "All fields are required!")
#             return

#         # Here you can add DB verification if needed.
#         open_student_dashboard(root, name)

#     tk.Button(
#         form_frame,
#         text="Login",
#         bg=ACCENT_COLOR,
#         fg="white",
#         font=("Poppins", 13, "bold"),
#         width=18,
#         height=1,
#         command=login,
#         relief="flat",
#         cursor="hand2"
#     ).pack(pady=30)

#     # Footer
#     tk.Label(
#         root,
#         text="© 2025 Techno India Group Public School | All Rights Reserved",
#         bg=BG_COLOR,
#         fg="#888",
#         font=("Poppins", 10)
#     ).pack(side="bottom", pady=15)

#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from dashboard.student_dashboard import open_student_dashboard
from styles.theme import *
from modules.marks import *


def open_student_login(parent=None):
    if parent:
        parent.destroy()

    root = tk.Tk()
    root.title("Student Login - Techno India Group Public School")
    root.state("zoomed")
    root.configure(bg=BG_COLOR)

    # ====== HEADER ======
    header = tk.Frame(root, bg=HEADER_BG, height=150)
    header.pack(fill="x")

    # Load school logo
    try:
        logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
        logo_path = os.path.abspath(logo_path)
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((130, 110), Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header, image=logo, bg=HEADER_BG)
        logo_label.image = logo
        logo_label.place(x=40, y=20)
    except Exception as e:
        print("⚠️ Logo Error:", e)
        tk.Label(header, text="[Logo Missing]", bg=HEADER_BG, fg=TEXT_COLOR, font=("Poppins", 16, "bold")).place(x=40, y=55)

    # School title
    tk.Label(
        header,
        text="Techno India Group Public School",
        bg=HEADER_BG,
        fg=TEXT_COLOR,
        font=("Poppins", 28, "bold")
    ).place(x=220, y=45)

    tk.Label(
        header,
        text="Student Login Portal",
        bg=HEADER_BG,
        fg="#333333",
        font=("Poppins", 14, "italic")
    ).place(x=220, y=100)

    # ====== LOGIN FORM ======
    form_frame = tk.Frame(root, bg=BG_COLOR)
    form_frame.pack(expand=True)

    tk.Label(
        form_frame,
        text="Student Login",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Poppins", 26, "bold")
    ).pack(pady=30)

    entries = {}
    fields = ["Name", "Roll No", "Class", "Password"]
    for field in fields:
        tk.Label(
            form_frame,
            text=field,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Poppins", 14, "bold")
        ).pack(pady=(10, 2))
        entry = tk.Entry(
            form_frame,
            font=("Poppins", 13),
            show="*" if field == "Password" else "",
            width=30,
            relief="flat",
            bd=2,
            highlightbackground="#ccc",
            highlightthickness=1
        )
        entry.pack(pady=5)
        entries[field] = entry

    # ====== BUTTONS ======
    def login():
        if all(e.get().strip() for e in entries.values()):
            open_student_dashboard(root, entries["Name"].get())
        else:
            messagebox.showerror("Error", "All fields are required!")

    login_btn = tk.Button(
        form_frame,
        text="Login",
        bg=ACCENT_COLOR,
        fg="white",
        font=("Poppins", 13, "bold"),
        width=18,
        height=1,
        relief="flat",
        cursor="hand2",
        command=login
    )
    login_btn.pack(pady=30)

    # Add hover effect
    def on_enter(e): login_btn.config(bg="#B52B2B")
    def on_leave(e): login_btn.config(bg=ACCENT_COLOR)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)

    # ====== BACK BUTTON ======
    def go_back():
        root.destroy()
        from main import main_window   # ✅ imported here to avoid circular import
        main_window()

    tk.Button(
        form_frame,
        text="← Back to Main Page",
        bg="#444",
        fg="white",
        font=("Poppins", 11, "bold"),
        width=20,
        relief="flat",
        cursor="hand2",
        command=go_back
    ).pack()

    # ====== FOOTER ======
    footer = tk.Label(
        root,
        text="© 2025 Techno India Group Public School | Developed by Soumya Subhra Ghosh",
        bg=HEADER_BG,
        fg="black",
        font=("Poppins", 10)
    )
    footer.pack(side="bottom", fill="x", ipady=5)

    root.mainloop()
