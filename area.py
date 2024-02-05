"""	Опишите функцию calculate_area,
 которая принимает два аргумента width и height и
  возвращает площадь прямоугольника. Удостоверьтесь,
   что функция работает для целых чисел и чисел с плавающей точкой."""


def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    - width (int or float): The width of the rectangle.
    - height (int or float): The height of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    area = width * height
    return area

# Примеры использования:

# Для целых чисел
integer_width = 5
integer_height = 10
result_integer = calculate_area(integer_width, integer_height)
print(f"Площадь прямоугольника с целыми числами: {result_integer}")

# Для чисел с плавающей точкой
float_width = 3.5
float_height = 8.2
result_float = calculate_area(float_width, float_height)
print(f"Площадь прямоугольника с числами с плавающей точкой: {result_float}")

