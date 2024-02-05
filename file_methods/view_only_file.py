import os

def view_files():
    directory = os.getcwd()
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory):
        print(f"Каталог {directory} не существует.")
        return
    
    # Получаем список всех элементов в указанном каталоге
    all_items = os.listdir(directory)
    
    # Создаем пустой список для хранения файлов
    files = []
    
    # Отбираем только папки
    for item in all_items:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item)
    
    # Выводим список папок
    print(f"Файлы в каталоге {directory}:")
    for file in files:
        print(file)
