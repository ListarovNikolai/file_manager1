import os


def make_dir():
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")

    new_dir = input("Введите название новой папки: ")
    if os.path.exists(new_dir):
        print(f"Папка по пути {new_dir} существует.")
    else:
        #print(f"Папка по пути {new_dir} не существует.")
        os.makedirs(new_dir)
        print(f"Создана новая папка {new_dir}")