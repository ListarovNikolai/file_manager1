import os

def view_subdir():
    directory = os.getcwd()
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory):
        print(f"Каталог {directory} не существует.")
        return
    
    # Получаем список всех элементов в указанном каталоге
    all_items = os.listdir(directory)
    
    # Создаем пустой список для хранения папок
    folders = []
    
    # Отбираем только папки
    for item in all_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    
    # Выводим список папок
    print(f"Папки в каталоге {directory}:")
    for folder in folders:
        print(folder)

