"""
Графический интерфейс приложения «Генератор надежных паролей».

Модуль создает окно приложения, получает параметры генерации
от пользователя и отображает созданный пароль.
"""

from tkinter import END, IntVar, Tk, ttk

import gen_pass

root = Tk()
root.title("Генератор паролей")
root.geometry("400x250")
root.resizable(False, False)

# Переменные для чекбоксов
var_digits = IntVar()
var_letters_lower = IntVar()
var_letters_upper = IntVar()
var_special = IntVar()

# Чекбоксы
check_digits = ttk.Checkbutton(text="Вкл. цифры", variable=var_digits)
# Цифры в пароле включены по умолчанию
var_digits.set(1)
check_letters_lower = ttk.Checkbutton(
    text="Вкл. строчные буквы", variable=var_letters_lower
)
check_letters_upper = ttk.Checkbutton(
    text="Вкл. прописные буквы", variable=var_letters_upper
)
check_special = ttk.Checkbutton(text="Вкл. спец. символы",
                                variable=var_special)

# Чекбоксы в первой строке
check_digits.grid(row=1, column=0, padx=20, pady=(40, 0), sticky="w")
check_letters_lower.grid(row=2, column=0, padx=20, pady=0, sticky="w")
check_letters_upper.grid(row=2, column=1, padx=0, pady=0, sticky="w")
check_special.grid(row=1, column=1, padx=0, pady=(40, 0), sticky="w")

# Поле ввода длины пароля
length_label = ttk.Label(root, text="Длина пароля:")
length_entry = ttk.Entry(root, width=10)
# Длина пароля по умолчанию
length_entry.insert(0, 6)

length_label.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="w")
length_entry.grid(row=3,
                  column=0, columnspan=2,
                  padx=110, pady=(20, 0),
                  sticky="w")

# Поле для вывода пароля
password_label = ttk.Label(root, text="Ваш пароль:")
password_entry = ttk.Entry(root, width=30)

password_label.grid(row=4, column=0, padx=20, pady=0, sticky="w")
password_entry.grid(row=4, column=0, columnspan=3,
                    padx=100, pady=5,
                    sticky="w")

status_label = ttk.Label(root, text="---")
status_label.grid(row=5, column=0, columnspan=3, padx=20, pady=0, sticky="n")


def copy_password():
    """
    Копирует сгенерированный пароль в буфер обмена.
    """
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()


def generate_password():
    """
    Получает параметры генерации из интерфейса,
    проверяет введенные данные и выводит созданный пароль.
    """
    length_text = length_entry.get()
    # проверяем, что введено целое число
    if not length_text.isdigit():
        # Очищаем поле и пишем ошибку
        password_entry.delete(0, END)
        password_entry.insert(0, "Введите число!")
        return

    length = int(length_text)
    use_digits = bool(var_digits.get())
    use_letters_lower = bool(var_letters_lower.get())
    use_letters_upper = bool(var_letters_upper.get())
    use_special = bool(var_special.get())

    # Проверка: выбран ли хотя бы один чекбокс
    if not (
            use_digits or use_letters_lower
            or use_letters_upper or use_special
    ):
        password_entry.delete(0, END)
        password_entry.insert(0, "Выберите типы символов!")
        return

    # Получаем пароль
    generated_password, status = gen_pass.gen_pass(
        use_digits, use_letters_lower,
        use_letters_upper, use_special,
        pass_len=length
    )

    # Выводим пароль в текстовое поле
    password_entry.delete(0, END)  # Очищаем поле
    password_entry.insert(0, generated_password)  # Вставляем новый текст
    status_label.config(text=status)


# Кнопка генерировать пароль
generate_btn = ttk.Button(root, text="Генерировать", command=generate_password)
generate_btn.grid(row=3, column=1, padx=40, pady=(20, 0), sticky="w")

# Кнопка копировать пароль
copy_btn = ttk.Button(root, text="Копировать", command=copy_password)
copy_btn.grid(row=4, column=1, sticky="w", padx=110)


if __name__ == "__main__":
    root.mainloop()
