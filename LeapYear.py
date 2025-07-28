def is_leap_year_short(year):
    """Проверяет високосность года (короткая версия)."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

