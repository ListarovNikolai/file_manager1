def area(width):
    """
    Calculate the area of a rectangle.

    Parameters:
    - width (int or float): The width of the rectangle.
    - height (int or float): The height of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    area = width ** 2
    return area


def perimeter(width):
    """Вычесления периметра квадрата """


    scquare_perimeter = width * 4
    return scquare_perimeter

if __name__ == "__main__":
    print("площадь квадрата: ", area(2))
    print("посчитаем периметр квадрата: ", perimeter(4))