from datetime import datetime

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