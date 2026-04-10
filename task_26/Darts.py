from math import sqrt
def score(x, y):
    distance = sqrt(x ** 2 + y ** 2)
    # Определяем количество очков в зависимости от расстояния
    if distance > 10:
        return 0  # Промах — за пределами мишени
    elif distance > 5:
        return 1  # Внешний круг
    elif distance > 1:
        return 5  # Средний круг
    else:
        return 10
