def caluclate_avg(iter):
    return sum(iter) / len(iter)

students_info = {}
number_of_students = int(input())
for _ in range(number_of_students):
    student_name, grade = input().split()
    grade = float(grade)
    if student_name not in students_info:
        students_info[student_name] = [grade]
    else:
        students_info[student_name].append(grade)
for key, value in students_info.items():
    value = tuple(value)
    avg_value = caluclate_avg(value)
    print(f"{key} -> ", end="")
    for grade in value:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {avg_value:.2f})")

