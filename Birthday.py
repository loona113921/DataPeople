from datetime import datetime
# Запрашиваем у пользователя день, месяц и год рождения
from calendar import leapdays

day = input("Введите день вашего рождения (число): ")
month = input("Введите месяц вашего рождения (название): ")
year = int(input("Введите год вашего рождения: "))

# Выводим результат
print(f"\nВаша дата рождения: {day} {month} {year} ")

# year = int(year)

def is_leap_year_short(year):
    """Проверяет високосность года (короткая версия)."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if is_leap_year_short(year) == True:
    print(f"\nГод {year} высокосный")
else:
    print(f"\nГод {year} не высокосный")


    digit_patterns = {
        '0': [
            '***',
            '* *',
            '* *',
            '* *',
            '***'
        ],
        '1': [
            ' * ',
            ' * ',
            ' * ',
            ' * ',
            ' * '
        ],
        '2': [
            '***',
            '  *',
            '***',
            '*  ',
            '***'
        ],
        '3': [
            '***',
            '  *',
            '***',
            '  *',
            '***'
        ],
        '4': [
            '* *',
            '* *',
            '***',
            '  *',
            '  *'
        ],
        '5': [
            '***',
            '*  ',
            '***',
            '  *',
            '***'
        ],
        '6': [
            '***',
            '*  ',
            '***',
            '* *',
            '***'
        ],
        '7': [
            '***',
            '  *',
            '  *',
            '  *',
            '  *'
        ],
        '8': [
            '***',
            '* *',
            '***',
            '* *',
            '***'
        ],
        '9': [
            '***',
            '* *',
            '***',
            '  *',
            '***'
        ],
        ' ': [
            ' ',
            ' ',
            ' ',
            ' ',
            ' '
        ]
    }

def print_date_in_digital_format(date_str):
        # Разбиваем дату на отдельные символы (дд мм гггг)
        digits = list(date_str)
    
        # Для каждой из 5 строк в шаблоне цифры
        for i in range(5):
            line = []
            for d in digits:
                if d in digit_patterns:
                    line.append(digit_patterns[d][i])
                else:
                    line.append('   ')  # Для неизвестных символов (например, разделителей)
    
            # Соединяем все цифры в строку с пробелами между ними
            print(' '.join(line))
    

birth_date = "23 04 1986"
print_date_in_digital_format(birth_date)
    
    

    
def calculate_age(birth_day, birth_month, birth_year):
    today = datetime.now()
        # Вычисляем разницу в годах
    age = today.year - birth_year
    
        # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age
    
    
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения (1-12): "))
year = int(input("Введите год рождения: "))
    
age = calculate_age(day, month, year)
print(f"Вам {age} лет.")
    

    
def get_weekday(day, month, year):
        
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

