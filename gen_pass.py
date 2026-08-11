import random
import string

def gen_pass(digits, letters, special, pass_len):
    pass_len = pass_len if pass_len > 0 else None

    # Собираем символы: буквы, цифры и символы
    characters = ""
    if digits:
        char_0 = string.digits
        characters += char_0
    if letters:
        char_1 = string.ascii_letters
        characters += char_1
    if special:
        char_2 = string.punctuation
        characters += char_2
    if not digits and not letters and not special:
        return 0
    # characters = char_0 + char_1 + char_2

    # Генерируем пароль нужной длины с помощью случайного выбора
    password = ''.join(random.choice(characters) for _ in range(pass_len))

    # print(password)
    return password