import os


def get_listdir():

    # Получение текущей рабочей директории
    current_directory = os.getcwd()
    print("Содержимое текущей рабочей директории:", current_directory)

    # Получение списка всех элементов в текущей директории
    all_items = os.listdir(current_directory)

    # Создание списка поддиректорий (папок)
    subdirectories = []
    for item in all_items:
        full_path = os.path.join(current_directory, item)
        if os.path.isdir(full_path):
            subdirectories.append(item)

    if subdirectories:
        print("Поддиректории (папки):")
        for subdir in subdirectories:
            print(subdir)
    else:
        print("В текущей директории нет поддиректорий (папок).")
