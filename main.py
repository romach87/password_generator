from tkinter import Tk, ttk, IntVar

import gen_pass

root = Tk()
root.title("Генератор паролей")
root.geometry("500x350")
root.resizable(False, False)

# Переменные для чекбоксов
var_digits = IntVar()
var_letters = IntVar()
var_special = IntVar()

# Чекбоксы
check_digits = ttk.Checkbutton(text="Вкл. цифры", variable=var_digits)
check_letters = ttk.Checkbutton(text="Вкл. буквы", variable=var_letters)
check_special = ttk.Checkbutton(text="Вкл. спец. символы", variable=var_special)

# Чекбоксы в первой строке
check_digits.grid(row=0, column=0, padx=20, pady=20, sticky="w")
check_letters.grid(row=0, column=1, padx=10, pady=20, sticky="w")
check_special.grid(row=0, column=2, padx=20, pady=20, sticky="w")

# Поле ввода длины пароля
length_label = ttk.Label(root, text="Длина пароля:")
length_entry = ttk.Entry(root, width=10)

length_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
length_entry.grid(row=1, column=1, padx=5, pady=10, sticky="w")

def generate_password():
    length_text = length_entry.get()
    # проверяем, что введено целое число
    if not length_text.isdigit():
        print("Пожалуйста, введите корректную длину пароля (целое число).")
        return

    length = int(length_text)
    use_digits = bool(var_digits.get())
    use_letters = bool(var_letters.get())
    use_special = bool(var_special.get())

    # пока просто вывод в консоль
    gen_pass.gen_pass(use_digits, use_letters, use_special,pass_len = length)
    print(f"Генерируем пароль длиной {length}, цифры={use_digits}, буквы={use_letters}, спецсимволы={use_special}")

generate_btn = ttk.Button(root, text="Генерировать", command=generate_password)
generate_btn.grid(row=1, column=2,  pady=20, sticky="w")

if __name__ == "__main__":
    root.mainloop()
