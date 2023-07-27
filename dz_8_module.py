from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now()

    # Знаходимо дату через тиждень
    week_later_date = current_date + timedelta(days=7)

    # Список для збереження користувачів, яких потрібно привітати по днях
    birthdays_per_week = {}
    for i in range(7):
        birthdays_per_week[i] = []

    # Перебираємо користувачів, перетворюємо дати на тип datetime з часом 00:00:00
    for user in users:
        user["birthday"] = datetime(
            user["birthday"].year, user["birthday"].month, user["birthday"].day
        )

    # Перебираємо користувачів і додаємо їх до відповідних списків днів тижня
    for user in users:
        birthday = user["birthday"]
        name = user["name"]

        # Виправлення: Якщо день народження вихідний, то привітати його в понеділок
        if current_date <= birthday < week_later_date:
            day_of_week = birthday.weekday()

            if day_of_week >= 5:  # Вихідний день: субота (5) або неділя (6)
                day_of_week = 0  # Переносимо на понеділок

            # Виправлення: Використовуємо індекси, які відповідають дням тижня
            birthdays_per_week[day_of_week].append(name)

    # Ім'я днів тижня для форматування результату
    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Виводимо результат у консоль
    for day_index, names in birthdays_per_week.items():
        if names:
            day_name = day_names[day_index]
            names_str = ", ".join(names)
            print(f"{day_name}: {names_str}")


# Приклад тестових даних:
users = [
    {"name": "Bill", "birthday": datetime(2023, 8, 1)},
    {"name": "Jill", "birthday": datetime(2023, 8, 2)},
    {"name": "Kim", "birthday": datetime(2023, 8, 3)},
    {"name": "Jan", "birthday": datetime(2023, 7, 30)},
    {"name": "Bob", "birthday": datetime(2023, 7, 24)},
    {"name": "Sam", "birthday": datetime(2023, 7, 31)},
    {"name": "Mike", "birthday": datetime(2023, 7, 29)},
    {"name": "Viki", "birthday": datetime(2023, 7, 28)},
]

if __name__ == "__main__":
    get_birthdays_per_week(users)
