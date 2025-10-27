# modules/profile.py
import tkinter as tk
from tkinter import messagebox
from styles.theme import *
from database import db_setup

def open_student_profile(parent, student_name):
    top = tk.Toplevel(parent)
    top.title("My Profile - Student")
    top.geometry("520x420")
    top.configure(bg=BG_COLOR)

    row = db_setup.get_student_profile(student_name)
    if not row:
        messagebox.showinfo("Profile", "Profile not found.")
        return

    tk.Label(top, text="Edit Student Profile", bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 14, "bold")).pack(pady=8)

    fields = {
        "Name": tk.StringVar(value=row["name"]),
        "Class": tk.StringVar(value=row["class"]),
        "Roll": tk.StringVar(value=row["roll"]),
        "Password": tk.StringVar(value=row["password"]),
        "Phone": tk.StringVar(value=row["phone"] or ""),
        "Email": tk.StringVar(value=row["email"] or "")
    }

    for k, v in fields.items():
        tk.Label(top, text=k, bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 11)).pack()
        e = tk.Entry(top, textvariable=v, font=("Poppins", 11))
        e.pack(pady=4)

    def save():
        db_setup.update_student_profile(row["id"], fields["Name"].get(), fields["Class"].get(),
                                        fields["Roll"].get(), fields["Password"].get(),
                                        fields["Phone"].get(), fields["Email"].get())
        messagebox.showinfo("Saved", "Profile updated.")
        top.destroy()

    tk.Button(top, text="Save Profile", bg=ACCENT_COLOR, fg="white", font=BUTTON_FONT, width=18, command=save).pack(pady=12)


def open_teacher_profile(parent, teacher_name):
    """Open teacher profile window for viewing/editing."""
    top = tk.Toplevel(parent)
    top.title("My Profile - Teacher")
    top.geometry("520x420")
    top.configure(bg=BG_COLOR)

    # --- Fetch teacher info ---
    try:
        row = db_setup.get_teacher_profile(teacher_name)
    except Exception as e:
        print("DB Error:", e)
        messagebox.showerror("Database Error", str(e))
        top.destroy()
        return

    # --- Handle missing teacher ---
    # if not row:
    #     print(f"DEBUG: Teacher profile not found for: {teacher_name}")
    #     messagebox.showerror("Not Found", f"No profile found for {teacher_name}")
    #     top.destroy()
    #     return

    # --- Header ---
    tk.Label(
        top, text="Edit Teacher Profile", bg=BG_COLOR, fg=TEXT_COLOR,
        font=("Poppins", 14, "bold")
    ).pack(pady=10)

    # --- Profile fields ---
    fields = {
        "Name": tk.StringVar(value=row["name"]),
        "Subject": tk.StringVar(value=row["subject"] or ""),
        "Password": tk.StringVar(value=row["password"] or ""),
        "Phone": tk.StringVar(value=row["phone"] or ""),
        "Email": tk.StringVar(value=row["email"] or "")
    }

    for k, var in fields.items():
        tk.Label(top, text=k, bg=BG_COLOR, fg=TEXT_COLOR, font=("Poppins", 11)).pack(pady=(5, 0))
        tk.Entry(top, textvariable=var, font=("Poppins", 11), relief="solid", bd=1).pack(pady=(0, 5), ipadx=5, ipady=3)

    # --- Save button ---
    def save():
        try:
            db_setup.update_teacher_profile(
                row["id"],
                fields["Name"].get(),
                fields["Subject"].get(),
                fields["Password"].get(),
                fields["Phone"].get(),
                fields["Email"].get()
            )
            messagebox.showinfo("Saved", "Profile updated successfully.")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save profile:\n{e}")

    tk.Button(
        top, text="💾 Save Profile",
        bg=ACCENT_COLOR, fg="white",
        font=BUTTON_FONT, width=20, relief="flat", command=save
    ).pack(pady=20)

    # --- Optional Close button ---
    tk.Button(
        top, text="❌ Close", bg="#E11D48", fg="white",
        font=("Poppins", 10, "bold"), width=12, relief="flat", command=top.destroy
    ).pack(pady=5)