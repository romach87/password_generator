import random
import string

import check_pass


def gen_pass(digits, letters_lower, letters_upper, special, pass_len):
    pass_len = pass_len if pass_len > 0 else None

    # Собираем символы: буквы, цифры и символы
    characters = ""
    if digits:
        char_0 = string.digits
        characters += char_0
    if letters_lower:
        char_1 = string.ascii_lowercase
        characters += char_1
    if letters_upper:
        char_2 = string.ascii_uppercase
        characters += char_2
    if special:
        char_3 = string.punctuation
        characters += char_3
    if not digits and not letters_lower and not letters_upper and not special:
        return 0
    # characters = char_0 + char_1 + char_2


    # Генерируем пароль нужной длины с помощью случайного выбора
    password = ''.join(random.choice(characters) for _ in range(pass_len))

    status = check_pass.check_password(password, digits, letters_lower, letters_upper, special)

    # print(password)
    return password, status