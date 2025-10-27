# import db_setup

# def clear_marks_and_attendance():
#     conn = db_setup.get_conn()
#     cur = conn.cursor()

#     # Delete all rows from marks and attendance
#     cur.execute("DELETE FROM marks")
#     cur.execute("DELETE FROM attendance")

#     conn.commit()
#     conn.close()
#     print("✅ All data cleared from marks and attendance tables.")

# if __name__ == "__main__":
#     clear_marks_and_attendance()


import db_setup

print(db_setup.get_teacher_profile("Mr.Sen", "Physics"))  # Example usage

# import sqlite3

# conn = sqlite3.connect("school.db")
# cursor = conn.cursor()

# cursor.execute("DELETE FROM teachers;")
# conn.commit()

# print("✅ All records deleted from teachers table.")

# conn.close()
