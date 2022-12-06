# dictionary comprehension (creates a dict from iterable without loop)
import random
names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
student_score = {name: random.randint(50, 100) for name in names}
print(student_score)

# conditional dictionary comprehension
passed_students = {name: score for (name, score) in student_score.items() if score > 60}
print(passed_students)
