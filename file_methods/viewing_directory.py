import os


def viewing_directory():
    """
    Просмотр рабочей директории
    """
    # Получение текущей рабочей директории
    current_directory = os.getcwd()
    print("Содержимое текущей рабочей директории:", current_directory)

    # Вывод списка файлов и поддиректорий
    contents = os.listdir(current_directory)

    for item in contents:
        print(item)