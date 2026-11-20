"""Арифметические операции учебного калькулятора."""


def add(a: float, b: float) -> float:
    """Возвращает сумму a и b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a и b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение a и b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает частное a и b.

    Вызывает ZeroDivisionError с понятным сообщением при делении на ноль.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b


def power(base: float, exponent: int) -> float:
    """Возводит base в целую степень exponent без использования оператора **."""
    if not isinstance(exponent, int):
        raise TypeError("Показатель степени должен быть целым числом")
    result = 1.0
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result


def to_roman(n: int) -> str:
    """Конвертирует целое число от 1 до 3999 в римскую запись."""
    if not isinstance(n, int) or not (1 <= n <= 3999):
        raise ValueError("Число должно быть целым в диапазоне от 1 до 3999")

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num
