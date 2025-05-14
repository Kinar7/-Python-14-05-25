import tkinter as tk
from tkinter import Toplevel, Label,simpledialog

students = {
    "Кирилл": "Любит Котлин и забывает про дедлайны.",
    "Аламат": "Пишет код вслепую и вслепую его тестирует.",
    "Рамига": "Смотрит лекции на по 3 раза, понимает их с первого",
    "Амир": "Всегда онлайн. Никогда не отвечает.",
}

def show_info(event):
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected)
        info = students.get(name, "Информации нет.")

        win = Toplevel(app)
        win.title(name)

        label = Label(win, text=info, padx=20, pady=10)
        label.pack()

        def edit_info():
            new_info = simpledialog.askstring("Редактировать", "Введите инфу:", initialvalue=info)
            if new_info:
                students[name] = new_info
                label.config(text=new_info)

        Button(win, text="Редактировать", command=edit_info).pack(pady=10)

def add_student():
    name = simpledialog.askstring("Имя", "Введите имя:")
    if name and name not in students:
        info = simpledialog.askstring("Инфо", "Введите инфу:")
        students[name] = info if info else "Нет информации."
        listbox.insert(tk.END, name)

app = tk.Tk()
app.title("Одногруппники")

listbox = tk.Listbox(app, width=30, height=10)
for name in students:
    listbox.insert(tk.END, name)
listbox.pack(padx=10, pady=10)

listbox.bind("<Double-Button-1>", show_info)

add_button = tk.Button(app, text="Добавить", command=add_student)
add_button.pack(pady=10)

app.mainloop()