import math


def scale(max_, n):
    if max_ <= 0:
        raise ValueError()
    del_ = 1
    while max_ / n < 1 or math.ceil(max_ / n) / (max_ / n) > 1.2:
        del_ *= 10
        max_ *= 10

    max_ = math.ceil(max_ / n) * n

    step = max_ / n
    return tuple(k * step / del_ for k in range(n + 1))
