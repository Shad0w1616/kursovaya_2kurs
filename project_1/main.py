# import tkinter as tk
# from tkinter import messagebox, filedialog
# import shutil
# import os
# from db import init_and_populate_db
# from form_1d import Form1D
# from form_2d import Form2D

# class MainWindow:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Хромоматематическое моделирование — Вариант 3")
#         self.root.geometry("900x620")
        
#         self.current_db = "hmm_data.db"   # текущая база данных

#         # ==================== ГЛАВНОЕ МЕНЮ ====================
#         menubar = tk.Menu(self.root)
#         self.root.config(menu=menubar)

#         # Меню Данные
#         data_menu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Данные", menu=data_menu)
#         data_menu.add_command(label="Создать новую БД", command=self.create_new_db)
#         data_menu.add_command(label="Открыть БД...", command=self.open_db)
#         data_menu.add_separator()
#         # data_menu.add_command(label="Инициализировать текущую БД", 
#         #                      command=self.init_current_db)
#         # data_menu.add_separator()
#         data_menu.add_command(label="Выход", command=self.root.quit)

#         # Меню Визуализация
#         vis_menu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Визуализация", menu=vis_menu)
#         vis_menu.add_command(label="1D — Числа Фибоначчи по модулю", 
#                             command=self.open_1d)
#         vis_menu.add_command(label="2D — Ker(Разность квадратов чисел)", 
#                             command=self.open_2d)

#         # Меню Справка
#         help_menu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Справка", menu=help_menu)
#         help_menu.add_command(label="Содержание", command=self.show_help)
#         help_menu.add_separator()
#         help_menu.add_command(label="О программе", command=self.about)

#         # Главный экран
#         tk.Label(self.root, text="Хромоматематическое моделирование\nВариант 3", 
#                 font=("Arial", 18, "bold"), justify="center").pack(pady=80)
        
#         tk.Button(self.root, text="Открыть 1D — Фибоначчи по модулю", 
#                  width=45, height=3, font=("Arial", 11),
#                  command=self.open_1d).pack(pady=12)
        
#         tk.Button(self.root, text="Открыть 2D — Ker(Разность квадратов)", 
#                  width=45, height=3, font=("Arial", 11),
#                  command=self.open_2d).pack(pady=12)

#     # def init_current_db(self):
#     #     init_and_populate_db()
#     #     messagebox.showinfo("Успех", f"Текущая БД ({self.current_db}) успешно заполнена")

#     def create_new_db(self):
#         file_path = filedialog.asksaveasfilename(
#             defaultextension=".db",
#             filetypes=[("Database files", "*.db"), ("All files", "*.*")],
#             title="Создать новую базу данных"
#         )
#         if file_path:
#             # Копируем структуру текущей БД
#             if os.path.exists("hmm_data.db"):
#                 shutil.copy("hmm_data.db", file_path)
#             else:
#                 self.current_db = file_path
#                 init_and_populate_db()  # создаст новую
#             self.current_db = file_path
#             messagebox.showinfo("Создано", f"Новая БД создана:\n{file_path}")

#     def open_db(self):
#         file_path = filedialog.askopenfilename(
#             filetypes=[("Database files", "*.db"), ("All files", "*.*")],
#             title="Открыть базу данных"
#         )
#         if file_path and os.path.exists(file_path):
#             self.current_db = file_path
#             messagebox.showinfo("Открыто", f"Загружена БД:\n{file_path}\n\nТеперь формы будут работать с ней.")
#         else:
#             messagebox.showwarning("Ошибка", "Файл не выбран или не существует.")

#     def open_1d(self):
#         Form1D(self.root, db_path=self.current_db)

#     def open_2d(self):
#         Form2D(self.root, db_path=self.current_db)

#     def show_help(self):
#         messagebox.showinfo("Справка", "Используйте меню «Данные» → Открыть БД или Создать новую БД")

#     def about(self):
#         messagebox.showinfo("О программе", 
#             "(c)Степанов П.С., Москва, 2026\nВыражаю слова поддержки любимым родителям - Ирине Геннадиевне и Сергею Викторовичу, спасибо вам за то, что всегда рядом. Ваша помощь в трудные минуты неоценима, а мудрые советы помогают мне идти вперед. Я чувствую вашу любовь и поддержку каждый день!")

# if __name__ == "__main__":
#     app = MainWindow()
#     app.root.mainloop()
import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os
from db import init_and_populate_db
from form_1d import Form1D
from form_2d import Form2D

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Хромоматематическое моделирование — Вариант 3")
        self.root.geometry("900x620")
        
        self.current_db = "hmm_data.db"   # текущая база данных

        # ==================== ГЛАВНОЕ МЕНЮ ====================
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Меню Данные
        data_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Данные", menu=data_menu)
        data_menu.add_command(label="Создать новую БД", 
                             command=self.create_new_db, accelerator="Ctrl+N")
        data_menu.add_command(label="Открыть БД", 
                             command=self.open_db, accelerator="Ctrl+O")
        data_menu.add_separator()
        # data_menu.add_command(label="Инициализировать текущую БД\tCtrl+I", 
        #                      command=self.init_current_db, accelerator="Ctrl+I")
        # data_menu.add_separator()
        data_menu.add_command(label="Выход", command=self.root.quit, accelerator="Ctrl+Q")

        # Меню Визуализация
        vis_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Визуализация", menu=vis_menu)
        vis_menu.add_command(label="1D — Числа Фибоначчи по модулю", 
                            command=self.open_1d, accelerator="F4")
        vis_menu.add_command(label="2D — Ker(Разность квадратов чисел)", 
                            command=self.open_2d, accelerator="F5")

        # Меню Справка
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Содержание", command=self.show_help, accelerator="F1")
        help_menu.add_separator()
        help_menu.add_command(label="О программе", command=self.about, accelerator="F2")

        # Привязка горячих клавиш к root
        self.root.bind('<Control-n>', lambda e: self.create_new_db())
        self.root.bind('<Control-o>', lambda e: self.open_db())
        # self.root.bind('<Control-i>', lambda e: self.init_current_db())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.bind('<F4>', lambda e: self.open_1d())
        self.root.bind('<F5>', lambda e: self.open_2d())
        self.root.bind('<F1>', lambda e: self.show_help())
        self.root.bind('<F2>', lambda e: self.about())

        # Главный экран
        tk.Label(self.root, text="Хромоматематическое моделирование\nВариант 3", 
                font=("Arial", 18, "bold"), justify="center").pack(pady=80)
        
        tk.Button(self.root, text="Открыть 1D — Фибоначчи по модулю", 
                 width=45, height=3, font=("Arial", 11),
                 command=self.open_1d).pack(pady=12)
        
        tk.Button(self.root, text="Открыть 2D — Ker(Разность квадратов)", 
                 width=45, height=3, font=("Arial", 11),
                 command=self.open_2d).pack(pady=12)

    # def init_current_db(self):
    #     init_and_populate_db()
    #     messagebox.showinfo("Успех", f"Текущая БД ({self.current_db}) успешно заполнена")

    def create_new_db(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[("Database files", "*.db"), ("All files", "*.*")],
            title="Создать новую базу данных"
        )
        if file_path:
            # Копируем структуру текущей БД
            if os.path.exists("hmm_data.db"):
                shutil.copy("hmm_data.db", file_path)
            else:
                self.current_db = file_path
                init_and_populate_db()  # создаст новую
            self.current_db = file_path
            messagebox.showinfo("Создано", f"Новая БД создана:\n{file_path}")

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
        import os
        
        # Путь к help.html в той же директории, что и main.py
        help_file = os.path.join(os.path.dirname(__file__), 'help.html')
        
        # Проверяем существование файла
        if os.path.exists(help_file):
            webbrowser.open('file:///' + os.path.abspath(help_file))
        else:
            messagebox.showwarning("Файл не найден", 
                                f"Файл help.html не найден в директории:\n{os.path.dirname(__file__)}\n\nСоздайте файл справки.")

    def about(self):
        messagebox.showinfo("О программе", 
            "(c)Степанов П.С., Москва, 2026\nВыражаю слова поддержки любимым родителям - Ирине Геннадиевне и Сергею Викторовичу, спасибо вам за то, что всегда рядом. Ваша помощь в трудные минуты неоценима, а мудрые советы помогают мне идти вперед. Я чувствую вашу любовь и поддержку каждый день!")

if __name__ == "__main__":
    app = MainWindow()
    app.root.mainloop()