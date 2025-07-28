from datetime import datetime

def get_weekday(day, month, year):
    """Возвращает день недели для указанной даты."""
    try:
        # Создаём объект datetime
        date_obj = datetime(year=year, month=month, day=day)
        # Получаем день недели (0 - понедельник, 6 - воскресенье)
        weekday_num = date_obj.weekday()
        # Список названий дней недели
        weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        return weekdays[weekday_num]
    except ValueError:
        return "Ошибка: некорректная дата!"

# Пример использования:
day = int(input("Введите день: "))
month = int(input("Введите месяц (число от 1 до 12): "))
year = int(input("Введите год: "))

weekday = get_weekday(day, month, year)
print(f"Этот день был/будет {weekday}.")
