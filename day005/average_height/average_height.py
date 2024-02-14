student_heigths = (180, 124, 165, 173, 189, 169, 146)

total_height = 0
for height in student_heigths:
    total_height += height

total_students = 0
for student in student_heigths:
    total_students += 1

average_height = round(total_height/total_students)

print(f"total height = {total_height}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")