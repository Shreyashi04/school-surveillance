import db_setup

# # ====== STUDENTS ======
# students = [
#     ("Adrito Das", "XII", "1", "adrito123", "9876543210", "adrito@example.com"),
#     ("Arko Choudhuri", "XII", "2", "arko123", "9876543211", "arko@example.com"),
#     ("Dipra Chakrabarty", "XII", "3", "dipra123", "9876543212", "dipra@example.com"),
#     ("Ishan Bhattacharjee", "XII", "4", "ishan123", "9876543213", "ishan@example.com"),
#     ("Soumya Subhra Ghosh", "XII", "5", "soumya123", "9876543214", "soumya@example.com"),
#     ("Sourodeep Sarkar", "XII", "6", "sourodeep123", "9876543215", "sourodeep@example.com"),
# ]

# ====== TEACHERS ======
teachers = [
    ("Mr.Sen", "Physics", "teachphy@123", "9998887771", "sen.physics@school.com"),
    ("Mrs.Roy", "Chemistry", "teachchem@123", "9998887772", "roy.chem@school.com"),
    ("Mr.Dutta", "Mathematics", "teachmath@123", "9998887773", "dutta.math@school.com"),
    ("Ms.Kaur", "Computer Science", "teachcs@123", "9998887774", "kaur.cs@school.com"),
    ("Dr.Das", "Artificial Intelligence", "teachai@123", "9998887775", "das.ai@school.com"),
]


for t in teachers:
    db_setup.add_teacher(*t)

# # ====== INSERT DATA ======
# for s in students:
#     db_setup.add_student(*s)

# print("✅ Database populated successfully with 6 students and 5 teachers!")
