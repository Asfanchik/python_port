# square = []
# for x in range (1, 5):
#     square.append(x + 2)
# names = ['Alex', 'Beth', 'Caroline']
# short_name = [name for name in names if len(name) < 5]
# long_name = [name.upper() for name in names if len(name) > 5]
#
# import random
# students_score = {student:random.randint for student in names}
# passed_student = {student:score for (student, score) in students_score.items() if score >= 60}
student_dict = {"student": ["Angla", "James", "Lily"],
                "score": [56, 76, 98]
                }

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)