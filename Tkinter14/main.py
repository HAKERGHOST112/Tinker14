from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# Открытие
def insert_text():
    try:
        file_name = fd.askopenfilename()
        if not file_name:
            raise FileNotFoundError("Файл не выбран.")
        with open(file_name, 'r') as f:
            s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showinfo("Информация", "Файл не загружен.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

# Сохранение
def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        if not file_name:
            raise FileNotFoundError("Имя файла не указано.")
        with open(file_name, 'w') as f:
            s = text.get(1.0, END)
            f.write(s.strip())
    except FileNotFoundError:
        mb.showinfo("Информация", "Файл не сохранён.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

#очистка
def clear_text():
    text.delete(1.0, END)


def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)


root = Tk()
root.title("Файловый менеджер")
root.geometry("500x400")

# Текстовое поле
text = Text(root, width=60, height=20)
text.grid(column=0, row=0, pady=10, padx=10)


mainmenu = Menu(root)
root.config(menu=mainmenu)

mainmenu.add_command(label="Открыть", command=insert_text)
mainmenu.add_command(label="Сохранить", command=extract_text)

#  меню очистить
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)

# Срабатывание при нажатии ПКМ
text.bind("<Button-3>", show_context_menu)

root.mainloop()
