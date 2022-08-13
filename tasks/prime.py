__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number < 2:
        return False
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
