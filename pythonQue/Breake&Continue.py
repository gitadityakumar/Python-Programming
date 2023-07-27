# now we are going to learn about continue and break

students = ["ram", "shyam", "rohan", "sohan", ]

for student in students:
    if student == "rohan":
        break;
    print(student)

for student in students:
    if student == "rohan":
        continue;
    print(student)
