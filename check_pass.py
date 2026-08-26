"""
Модуль проверки паролей.

"""


def check_password(password, digits, letters_lower, letters_upper, special):
    result = ""
    count = 0
    if len(password) >= 8:
        count += 1
    if len(password) >= 12:
        count += 2
    if letters_lower:
        count += 1
    if letters_upper:
        count += 1
    if special:
        count += 1

    if count == 0:
        result = "Пароль опасный!"
    if count == 1 or count == 2:
        result = "Слабый пароль!"
    if count == 3 or count == 4:
        result = "Нормальный пароль!"
    if count == 5 or count == 6:
        result = "Отличный пароль!"

    return result
