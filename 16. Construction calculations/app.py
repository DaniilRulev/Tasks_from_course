"""Основная программа для решения задачи"""


brick_lwh = (250, 120, 65)         # Размеры кирпича: длина, ширина, высота (мм) .
mortar = 10                        # Толщина слоя раствора для кладки (мм).
wall_lwh = (10000, 510, 3000)      # Размеры стены: длина, толщина, высота (мм) .


from calc.primitives.rectangle import get_volume, get_meters
from calc.rectangle import count_volumes, volume_solution


wall_volume_mm = get_volume(*wall_lwh)
wall_volume = get_meters(wall_volume_mm)

brick_volume_mm = get_volume(*brick_lwh, gap=mortar)
brick_volume_without_gap = get_volume(*brick_lwh)
bricks_count = count_volumes(brick_volume_mm, wall_volume_mm)

solution = volume_solution(bricks_count, brick_volume_without_gap, wall_volume_mm)

print(f"Объем стены: {wall_volume} м3.")
print(f"Количество кирпичей: {bricks_count}.")
print(f"Количество раствора: {solution} литров.")