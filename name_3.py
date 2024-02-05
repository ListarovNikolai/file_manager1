"""1.	Создайте функцию get_full_name,
 которая принимает два обязательных параметра first_name и last_name
  и возвращает полное имя в формате "Имя Фамилия", причем оба компонента должны
   начинаться с заглавной буквы, даже если введены с маленькой.
"""


def get_full_name(first_name, last_name, middle_name=" "):
    full_name = first_name.capitalize() + " " + last_name.capitalize() + " " + middle_name.capitalize()
    return full_name


name = get_full_name("николай", "листаров", "дмитриевич")
print(name)
