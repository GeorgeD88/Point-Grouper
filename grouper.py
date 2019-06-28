import math


def get_average(points: list) -> tuple:
    x_avg = 0
    y_avg = 0
    length = len(points)
    for x, y in points:
        x_avg += x
        y_avg += y
    x_avg = x_avg/length
    y_avg = y_avg/length
    return x_avg, y_avg


def origin_distance(pair: tuple) -> float or int:
    distance = math.hypot(pair[0], pair[1])
    return distance if not str(distance).endswith('.0') else int(str(distance)[:-2])  # Strips the unnecessary zero from the float if needed.
