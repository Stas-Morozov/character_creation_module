from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Проверяет введенное значение."""
    if your_number <= 0:
        print('Не можем обработать ноль или отрицательное значение')
    else:
        sqrt_calc = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {sqrt_calc}')


calc(25.5)
