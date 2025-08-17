import tkinter as tk
from tkinter import messagebox
import sys
import os
from config import password

def lock_computer():
    PASSWORD = password  # Пароль для разблокировки
    
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="black")
    root.title("LOCKED")

    # Основные элементы интерфейса
    label = tk.Label(
        root,
        text="КОМПЬЮТЕР ЗАБЛОКИРОВАН\nОбратитесь к администратору",
        font=("Arial", 40, "bold"),
        fg="red",
        bg="black"
    )
    label.pack(expand=True)

    password_entry = tk.Entry(root, show="*", font=("Arial", 24))
    password_entry.pack(pady=20)
    password_entry.focus()

    def check_password():
        if password_entry.get() == PASSWORD:
            root.destroy()
            sys.exit(0)  # Успешный выход
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")
            password_entry.delete(0, tk.END)

    tk.Button(
        root,
        text="Разблокировать",
        command=check_password,
        font=("Arial", 20),
        bg="gray",
        fg="white"
    ).pack(pady=10)

    # Блокировка системных комбинаций
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.bind("<Alt-F4>", lambda e: None)
    root.bind("<Control-Alt-Delete>", lambda e: None)
    
    root.mainloop()

if __name__ == "__main__":
    lock_computer()