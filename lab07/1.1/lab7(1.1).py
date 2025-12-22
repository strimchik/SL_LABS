import pickle

students = {
    "Иванов": {"Математика": 8, "Физика": 7, "Химия": 9, "История": 8, "Информатика": 9},
    "Петров": {"Математика": 7, "Физика": 8, "Химия": 7, "История": 8, "Информатика": 8},
    "Сидоров": {"Математика": 9, "Физика": 8, "Химия": 9, "История": 9, "Информатика": 8},
    "Кузнецова": {"Математика": 6, "Физика": 9, "Химия": 8, "История": 7, "Информатика": 9},
    "Смирнов": {"Математика": 10, "Физика": 9, "Химия": 10, "История": 8, "Информатика": 10},
    "Попова": {"Математика": 8, "Физика": 8, "Химия": 8, "История": 8, "Информатика": 8},
    "Васильев": {"Математика": 5, "Физика": 6, "Химия": 7, "История": 6, "Информатика": 7}
}


for student, scores in students.items():
    print(f"\n{student}:")
    for subject, score in scores.items():
        print(f"  {subject}: {score}")

average_scores = {}
for student, scores in students.items():
    avg_score = sum(scores.values()) / len(scores)
    average_scores[student] = avg_score



max_student = max(average_scores, key=average_scores.get)
min_student = min(average_scores, key=average_scores.get)
print(f"Максимальный: {max_student}")
print(f"Минимальный: {min_student}")

math_scores = [scores["Математика"] for scores in students.values()]
average_math = sum(math_scores) / len(math_scores)


above_average_math = []
for student, scores in students.items():
    if scores["Математика"] > average_math:
        above_average_math.append((student, scores["Математика"]))


with open('data.pickle', 'wb') as f:
    pickle.dump(students, f)


with open('data.pickle', 'rb') as f:
    loaded_students = pickle.load(f)
