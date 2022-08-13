__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    time = {'d': 3600 * 24, 'h': 3600, 'm': 60}
    s = ''
    for key, val in time.items():
        if seconds // val != 0 or s:
            s += str(seconds // val).rjust(2, '0') + key
            seconds %= val
    s += str(seconds % 60).rjust(2, '0') + 's'
    return s
