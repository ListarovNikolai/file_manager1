import guess
from pass_gen import generate_random_password
from task_3 import calculate_grade
from area import calculate_area


def show_menu():
    print("Меню:")
    print("1. Сгенерировать пароль")
    print("2. Игра в угадайку")
    print("3. Средний балл")
    print("4. Вычисление площади")
    print("5. Выход")


def main():
    while True:
        show_menu()

        choice = input("Выберите пункт меню (1-5): ")

        if choice == '1':
            password_length = int(input("Введите длину пароля: "))
            random_password = generate_random_password(password_length)
            print("Сгенерированный пароль:", random_password)

        elif choice == '2':
            guess.guess()

        elif choice == '3':
            student_grades = []
            for i in range(5):
                student_grades.append(int(input("Введите оценку: ")))
            #print(student_grades)
            result = calculate_grade(student_grades)
            if result[1] is not None:
                average, final_grade = result
                print(f"Средний балл: {average}, Итоговая оценка: {final_grade}")
            else:
                print(f"Ошибка: {result[0]}")

        elif choice == '4':
            width = float(input("Введите ширину: "))
            height = float(input("Введите длину: "))
            result = calculate_area(width, height)
            print(f"Площадь прямоугольника : {result}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 5.")


if __name__ == "__main__":
    main()
