students ={
    "a" : 40,
    "b" : 60,
    "c" : 70,
    "d" : 80,
    "e" : 90
}
all_scores = students.values()

average = sum(all_scores) / len(all_scores)
print(average)
top_student = max(students, key=students.get)

bottom_student = min(students, key=students.get)
print(top_student)
print(bottom_student)