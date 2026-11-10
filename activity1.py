
grades = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

print("Student Grade Book")

total = 0
count = 0
for score in grades.values():
    total = total + score
    count = count + 1

average = total / count
print("Class average:", average)

highest = max(grades.values())
lowest = min(grades.values())

for name in grades:
    if grades[name] == highest:
        top_student = name
    if grades[name] == lowest:
        bottom_student = name

print("Top scorer:", top_student, "with", highest)
print("Bottom scorer:", bottom_student, "with", lowest)

print()
search = input("Enter a student name to look up: ")

score = grades.get(search)

if score is None:
    print("Sorry, that student is not in the grade book.")
else:
    print(search, "got a score of", score)
