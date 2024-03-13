from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji

if __name__ == '__main__':
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Текущая дата: {current_date}")

    current_time = datetime.datetime.now().timestamp()
    print(f"Текущее время в секундах с начала эпохи: {current_time}")

    print("Вызываем функцию calculate_salary из модуля salary.py:")
    calculate_salary()

    print("Вызываем функцию get_employees из модуля people.py:")
    get_employees()

    print(emoji.emojize("Python is fun :red_heart:"))