import math


def area(radius):

    """
    Calculate the area of a circle.

    Parameters:
    radius

    Returns:
    - float: The area of the rectangle.
    """
    area = math.pi * radius ** 2
    return area


def perimeter(radius):
    """Вычесления периметра квадрата """

    circle_perimeter = 2 * math.pi * radius
    return circle_perimeter


if __name__ == "__main__":
    print("площадь окружности: ", area(2))
    print("посчитаем периметр окружности: ", perimeter(1))