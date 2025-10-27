import tkinter as tk
from PIL import Image, ImageTk
import os
from login.student_login import open_student_login
from login.teacher_login import open_teacher_login
from styles.theme import *


def main_window():
    root = tk.Tk()
    root.title("Techno India Group Public School - Portal")
    root.state('zoomed')  # ✅ Opens full screen automatically
    root.configure(bg=BG_COLOR)

    # ====== Header Frame ======
    header = tk.Frame(root, bg=HEADER_BG, height=150)
    header.pack(fill="x")

    # ====== Load and Display Logo Safely ======
    try:
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo not found: {logo_path}")

        # Resize the logo to fit neatly in header
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((150, 125), Image.LANCZOS)  # ✅ Perfect size balance
        logo = ImageTk.PhotoImage(logo_img)

        logo_label = tk.Label(header, image=logo, bg=HEADER_BG)
        logo_label.image = logo  # ✅ Prevent garbage collection
        logo_label.place(x=40, y=10)

    except Exception as e:
        print("⚠️ Logo Load Error:", e)
        logo_label = tk.Label(header, text="[Logo Missing]",
                              bg=HEADER_BG, fg=TEXT_COLOR,
                              font=("Poppins", 16, "bold"))
        logo_label.place(x=40, y=45)

    # ====== School Title ======
    school_label = tk.Label(
        header,
        text="Techno India Group Public School",
        bg=HEADER_BG,
        fg=TEXT_COLOR,
        font=("Poppins", 30, "bold")
    )
    school_label.place(x=220, y=45)

    subtitle = tk.Label(
        header,
        text="Smart Surveillance & Performance Portal",
        bg=HEADER_BG,
        fg="#333333",
        font=("Poppins", 14, "italic")
    )
    subtitle.place(x=220, y=100)

    # ====== Main Content ======
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(expand=True, fill="both")

    tk.Label(
        frame,
        text="Select Your Role",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Poppins", 26, "bold")
    ).pack(pady=60)

    # ====== Buttons ======
    button_style = {
        "bg": ACCENT_COLOR,
        "fg": "white",
        "font": ("Poppins", 14, "bold"),
        "relief": "flat",
        "width": 25,
        "height": 2,
        "cursor": "hand2",
        "activebackground": "#B52B2B"
    }

    student_btn = tk.Button(
        frame,
        text="🎓 Student Login",
        command=lambda: open_student_login(root),
        **button_style
    )
    student_btn.pack(pady=20)

    teacher_btn = tk.Button(
        frame,
        text="👨‍🏫 Teacher Login",
        command=lambda: open_teacher_login(root),
        **button_style
    )
    teacher_btn.pack(pady=20)

    # ====== Footer ======
    footer = tk.Label(
        root,
        text="© 2025 Techno India Group Public School | Developed by Soumya Subhra Ghosh",
        bg=HEADER_BG,
        fg="black",
        font=("Poppins", 10)
    )
    footer.pack(side="bottom", fill="x", ipady=5)

    root.mainloop()

def open_main_page():
    main_window()



if __name__ == "__main__":
    main_window()
