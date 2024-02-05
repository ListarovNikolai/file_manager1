import os

def view_files(directory):
    # Получаем список всех файлов и поддиректорий в указанной директории
    items = os.listdir(directory)

    # Проходимся по каждому элементу
    for item in items:
        # Формируем полный путь к текущему элементу
        full_path = os.path.join(directory, item)

        # Проверяем, является ли элемент файлом
        if os.path.isfile(full_path):
            # Если это файл, выводим его полный путь
            print(full_path)
        
