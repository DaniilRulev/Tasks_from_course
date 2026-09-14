"""Файл с простыми функциями для работы с прямоугольниками."""


def get_volume(length: int | float, width: int | float, height: int | float, *, gap: int | float | None = None) -> int | float:
    """Возвращает объем параллелипипеда.
        - Параметр gap учитывает зазор.
        - Результат возвращается в мм^3."""

    if gap:
        length += gap
        width += gap
        height += gap

    volume = length * width * height
    return volume


def get_area(length: int | float, width: int | float, *_) -> int | float:
    """Возвращает площадь прямоугольника.
        - Результат возвращается в мм^3."""
    area = length * width
    return area


def get_meters(value: int | float, ndigits: int = 2) -> int | float:
    """Возвращает результат в кубических метрах.
        - Параметр ndigist - количество знаков после запятой"""
    meters_value = round(value / 1000000000, ndigits)
    
    return meters_value