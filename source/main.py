import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os
import sys
from source.config import TITLE, VERSION
from source.db import init_and_populate_db
from source.form_1d import Form1D
from source.form_2d import Form2D
from data.hmm_models import get_hmm_color  

# Базовые пути
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "data")
HELP_DIR = os.path.join(BASE_DIR, "help")

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(TITLE)
        self.root.geometry("900x620")
        self.current_db = os.path.join(DB_DIR, "hmm_data.db")
        #Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        data_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Данные", menu=data_menu)
        data_menu.add_command(label="Создать новую БД", 
                             command=self.create_new_db, accelerator="Ctrl+N")
        data_menu.add_command(label="Открыть БД", 
                             command=self.open_db, accelerator="Ctrl+O")
        data_menu.add_separator()
        data_menu.add_command(label="Выход", command=self.root.quit, accelerator="Ctrl+Q")

        vis_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Визуализация", menu=vis_menu)
        vis_menu.add_command(label="1D — Числа Фибоначчи по модулю", 
                            command=self.open_1d, accelerator="F4")
        vis_menu.add_command(label="2D — Ker(Разность квадратов чисел)", 
                            command=self.open_2d, accelerator="F5")

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Содержание", command=self.show_help, accelerator="F1")
        help_menu.add_separator()
        help_menu.add_command(label="О программе", command=self.about, accelerator="F2")

        self.root.bind('<Control-n>', lambda e: self.create_new_db())
        self.root.bind('<Control-o>', lambda e: self.open_db())
        # self.root.bind('<Control-i>', lambda e: self.init_current_db())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.bind('<F4>', lambda e: self.open_1d())
        self.root.bind('<F5>', lambda e: self.open_2d())
        self.root.bind('<F1>', lambda e: self.show_help())
        self.root.bind('<F2>', lambda e: self.about())

        tk.Label(self.root, text="Хромоматематическое моделирование\nВариант 3", 
                font=("Arial", 18, "bold"), justify="center").pack(pady=80)
        
        tk.Button(self.root, text="Открыть 1D — Фибоначчи по модулю", 
                 width=45, height=3, font=("Arial", 11),
                 command=self.open_1d).pack(pady=12)
        
        tk.Button(self.root, text="Открыть 2D — Ker(Разность квадратов)", 
                 width=45, height=3, font=("Arial", 11),
                 command=self.open_2d).pack(pady=12)

    def create_new_db(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[("Database files", "*.db"), ("All files", "*.*")],
            initialdir=DB_DIR,
            title="Создать новую базу данных"
        )
        if not file_path:
            return

        try:
            if os.path.exists(file_path):
                if not messagebox.askyesno("Файл существует", 
                    f"Файл {os.path.basename(file_path)} уже существует.\nПерезаписать?"):
                    return

            self.current_db = file_path
            init_and_populate_db(db_path=file_path)
            
            messagebox.showinfo("Успешно", 
                f"Новая база данных успешно создана:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Ошибка", 
                f"Не удалось создать базу данных:\n{str(e)}")
                
    def open_db(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Database files", "*.db"), ("All files", "*.*")],
            title="Открыть базу данных"
        )
        if file_path and os.path.exists(file_path):
            self.current_db = file_path
            messagebox.showinfo("Открыто", f"Загружена БД:\n{file_path}\n\nТеперь формы будут работать с ней.")
        else:
            messagebox.showwarning("Ошибка", "Файл не выбран или не существует.")

    def open_1d(self):
        Form1D(self.root, db_path=self.current_db)

    def open_2d(self):
        Form2D(self.root, db_path=self.current_db)

    def show_help(self):
        import webbrowser
        help_file = os.path.join(HELP_DIR, "help.html")
        if os.path.exists(help_file):
            webbrowser.open('file:///' + os.path.abspath(help_file))
        else:
            messagebox.showwarning("Файл не найден", f"help.html отсутствует в папке:\n{HELP_DIR}")

    def about(self):
        messagebox.showinfo("О программе", "(c)Степанов П.С., Москва, 2026\nВыражаю слова поддержки любимым родителям - Ирине Геннадиевне и Сергею Викторовичу, спасибо вам за то, что всегда рядом. Ваша помощь в трудные минуты неоценима, а мудрые советы помогают мне идти вперед. Я чувствую вашу любовь и поддержку каждый день!")

if __name__ == "__main__":
    app = MainWindow()
    app.root.mainloop()