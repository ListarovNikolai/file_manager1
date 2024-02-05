"""3.	Функция calculate_grade,
 которая принимает список оценок студента
  и возвращает его средний балл и соответствующую оценку
   (A, B, C, D, F).

"""
def calculate_grade(grades):
    if not grades:
        return "Список оценок не может быть пустым", None

    average_grade = sum(grades) / len(grades)

    if average_grade >= 90:
        grade = 'A'
    elif average_grade >= 80:
        grade = 'B'
    elif average_grade >= 70:
        grade = 'C'
    elif average_grade >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return average_grade, grade

# Пример использования
student_grades = [82,78,90,69,99]
result = calculate_grade(student_grades)

if result[1] is not None:
    average, final_grade = result
    print(f"Средний балл: {average}, Итоговая оценка: {final_grade}")
else:
    print(f"Ошибка: {result[0]}")
