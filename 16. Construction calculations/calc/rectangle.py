"""Функции для работы с прямоугольниками."""


from .primitives.rectangle import get_area, get_volume


def count_volumes(small: int | float, big: int | float) -> int:
    """Количество маленьких прямоугольников в большом.
        - Округление до целого!"""

    raw_count = big / small
    count = raw_count if (raw_count) % 1 == 0 else (raw_count // 1) + 1
    count = round(count)
    
    return count


def volume_solution(bricks: int, small: int | float, big: int | float) -> int | float:
    """Объем раствора необходимого для укладки кирпичей.
        - В small необходимо вставлять значение объема кирпича без учета раствора.
        - Результат возвращается в литрах!"""

    mm_volume = big - (bricks * small)
    volume = round(mm_volume / 1000000, 3)

    return volume