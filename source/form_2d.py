# import tkinter as tk
# from tkinter import ttk
# import sqlite3
# from data.hmm_models import get_hmm_color 

# class Form2D(tk.Toplevel):
#     def __init__(self, parent, db_path="hmm_data.db"):
#         super().__init__(parent)
#         self.db_path = db_path   # ← Главное изменение
        
#         self.title("Объект 2D: Ker(|X² - Y²|)")
#         self.geometry("1180x820")
#         self.minsize(1000, 700)

#         # Главный фрейм
#         main_frame = tk.Frame(self)
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

#         tk.Label(main_frame, text="Объект 2D: Ker(Разность квадратов чисел)", 
#                 font=("Arial", 16, "bold")).pack(pady=(0, 8))

#         # Левая панель параметров
#         left_frame = tk.Frame(main_frame, width=340)
#         left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
#         left_frame.pack_propagate(False)

#         param_frame = tk.LabelFrame(left_frame, text="Параметры моделирования", padx=12, pady=12)
#         param_frame.pack(fill=tk.BOTH, expand=True)

#         # ... (все параметры остаются как были) ...
#         tk.Label(param_frame, text="Модель НММ:").pack(anchor="w", pady=(0,4))
#         self.model_var = tk.StringVar(value="НММ_Rainbow")
#         ttk.Combobox(param_frame, textvariable=self.model_var, 
#                     values=["НММ_N", "НММ_N2", "НММ_Rainbow"], width=25, state="readonly").pack(anchor="w", pady=4)

#         tk.Label(param_frame, text="Aspect:").pack(anchor="w", pady=(8,4))
#         self.aspect_var = tk.DoubleVar(value=1.0)
#         tk.Entry(param_frame, textvariable=self.aspect_var, width=12).pack(anchor="w", pady=4)

#         # Диапазоны
#         range_f = tk.LabelFrame(param_frame, text="Диапазоны", padx=10, pady=8)
#         range_f.pack(fill=tk.X, pady=10)
#         # Xmin Xmax
#         tk.Label(range_f, text="Xmin:").grid(row=0,column=0,sticky="e",padx=4)
#         self.xmin_var = tk.IntVar(value=1); tk.Entry(range_f, textvariable=self.xmin_var,width=8).grid(row=0,column=1,padx=4)
#         tk.Label(range_f, text="Xmax:").grid(row=0,column=2,sticky="e",padx=4)
#         self.xmax_var = tk.IntVar(value=50); tk.Entry(range_f, textvariable=self.xmax_var,width=8).grid(row=0,column=3,padx=4)
#         # Ymin Ymax
#         tk.Label(range_f, text="Ymin:").grid(row=1,column=0,sticky="e",padx=4,pady=6)
#         self.ymin_var = tk.IntVar(value=1); tk.Entry(range_f, textvariable=self.ymin_var,width=8).grid(row=1,column=1,padx=4)
#         tk.Label(range_f, text="Ymax:").grid(row=1,column=2,sticky="e",padx=4,pady=6)
#         self.ymax_var = tk.IntVar(value=50); tk.Entry(range_f, textvariable=self.ymax_var,width=8).grid(row=1,column=3,padx=4)

#         tk.Label(param_frame, text="Опции:").pack(anchor="w", pady=(12,4))
#         self.value_var = tk.BooleanVar(value=False)
#         self.grid_var = tk.BooleanVar(value=True)
#         tk.Checkbutton(param_frame, text="Value", variable=self.value_var).pack(anchor="w")
#         tk.Checkbutton(param_frame, text="Grid", variable=self.grid_var).pack(anchor="w")

#         tk.Label(param_frame, text="Визуализация:").pack(anchor="w", pady=(15,4))
#         self.vis_var = tk.StringVar(value="Цветная матрица")
#         self.vis_combo = ttk.Combobox(param_frame, textvariable=self.vis_var,
#                                      values=["Цветная матрица", "По Ker", "Спираль 2D", "Градиентная"],
#                                      width=28, state="readonly")
#         self.vis_combo.pack(anchor="w", pady=4)

#         # ====================== КНОПКИ ======================
#         # Кнопка Применить
#         apply_btn_frame = tk.Frame(param_frame)
#         apply_btn_frame.pack(fill=tk.X, pady=(12, 6))
        
#         tk.Button(apply_btn_frame, text="Применить / Пересчитать", 
#                   font=("Arial", 11, "bold"), 
#                   command=self.apply_visualization).pack(fill=tk.X, padx=2)

#         # Кнопки Справка и Закрыть ниже
#         btn_frame = tk.Frame(param_frame)
#         btn_frame.pack(fill=tk.X, pady=(0, 12))

#         tk.Button(btn_frame, text="Справка", 
#                   font=("Arial", 10, "bold"), 
#                   command=self.show_help).pack(side=tk.LEFT, padx=(0, 8), fill=tk.X, expand=True)

#         tk.Button(btn_frame, text="Закрыть", 
#                   font=("Arial", 10, "bold"), 
#                   command=self.destroy).pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)

#         # ==================== Canvas с прокруткой ====================
#         canvas_frame = tk.Frame(main_frame)
#         canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#         # Scrollbars
#         v_scroll = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
#         h_scroll = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)

#         self.canvas = tk.Canvas(canvas_frame, bg="#0a0a0a", highlightthickness=2,
#                                highlightbackground="#555", 
#                                xscrollcommand=h_scroll.set,
#                                yscrollcommand=v_scroll.set)

#         v_scroll.config(command=self.canvas.yview)
#         h_scroll.config(command=self.canvas.xview)

#         self.canvas.grid(row=0, column=0, sticky="nsew")
#         v_scroll.grid(row=0, column=1, sticky="ns")
#         h_scroll.grid(row=1, column=0, sticky="ew")

#         canvas_frame.grid_rowconfigure(0, weight=1)
#         canvas_frame.grid_columnconfigure(0, weight=1)

#         self.bind("<Configure>", self.on_resize)
#         self.after(300, self.apply_visualization)

#     def on_resize(self, event=None):
#         if hasattr(self, 'current_vis'):
#             self.after(100, self.apply_visualization)

#     def apply_visualization(self):
#         self.current_vis = self.vis_var.get()
#         if self.current_vis == "Цветная матрица":
#             self.show_matrix()
#         elif self.current_vis == "По Ker":
#             self.show_by_ker()
#         elif self.current_vis == "Спираль 2D":
#             self.show_spiral_2d()
#         elif self.current_vis == "Градиентная":
#             self.show_gradient()

#     # ====================== СПРАВКА ======================
#     def show_help(self):
#         import webbrowser
#         import os
        
#         # Путь к help.html (основная справка по 2D визуализации)
#         help_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'help', 'help.html')
        
#         # Проверяем существование файла
#         if os.path.exists(help_file):
#             webbrowser.open('file:///' + os.path.abspath(help_file))
#         else:
#             # Пробуем найти в текущей директории
#             help_file = os.path.join(os.path.dirname(__file__), 'help.html')
#             if os.path.exists(help_file):
#                 webbrowser.open('file:///' + os.path.abspath(help_file))
#             else:
#                 messagebox.showwarning("Файл не найден", 
#                                     f"Файл help.html не найден.\n\nСоздайте файл справки в папке help/")

#         tk.Button(help_win, text="Закрыть", command=help_win.destroy, 
#                  font=("Arial", 10), width=12).pack(pady=10)

#     # ====================== ВИЗУАЛИЗАЦИИ ======================

#     def _draw_matrix(self, use_diff=False):
#         self.canvas.delete("all")
#         xmin, xmax = self.xmin_var.get(), self.xmax_var.get()
#         ymin, ymax = self.ymin_var.get(), self.ymax_var.get()
        
#         cols = xmax - xmin + 1
#         cell_w = 18
#         cell_h = int(cell_w * self.aspect_var.get())

#         total_w = cols * cell_w
#         total_h = (ymax - ymin + 1) * cell_h

#         conn = sqlite3.connect(self.db_path)
#         c = conn.cursor()
#         field = "diff" if use_diff else "ker"
#         c.execute(f"SELECT x, y, {field} FROM ker_diff WHERE x BETWEEN ? AND ? AND y BETWEEN ? AND ?",
#                   (xmin, xmax, ymin, ymax))

#         for x, y, value in c.fetchall():
#             color = get_hmm_color(value, self.model_var.get(), 
#                                 mod=9 if not use_diff else 120, 
#                                 max_val=9 if not use_diff else 1000)
            
#             px1 = (x - xmin) * cell_w
#             py1 = (y - ymin) * cell_h
#             px2 = px1 + cell_w
#             py2 = py1 + cell_h

#             self.canvas.create_rectangle(px1, py1, px2, py2,
#                                        fill=color, 
#                                        outline="#222222" if self.grid_var.get() else "")

#             # ==================== VALUE ====================
#             if self.value_var.get():
#                 # Более мягкие условия
#                 if cell_w >= 26 and cell_h >= 20:
#                     if value < 100:
#                         text = str(value)
#                         font_size = 10
#                     elif value < 1000 and cell_w >= 34:
#                         text = str(value)
#                         font_size = 9
#                     else:
#                         text = "●"
#                         font_size = 8
#                 elif cell_w >= 18 and cell_h >= 16:
#                     text = str(value)[:1] if value >= 100 else str(value)
#                     font_size = 8
#                 else:
#                     text = ""
#                     font_size = 7

#                 if text:
#                     self.canvas.create_text(
#                         (px1 + px2) // 2, (py1 + py2) // 2,
#                         text=text,
#                         fill="white",
#                         font=("Consolas", font_size, "bold")
#                     )

#         conn.close()
#         self.canvas.config(scrollregion=(0, 0, total_w, total_h))

#     def show_matrix(self):
#         self._draw_matrix(use_diff=True)

#     def show_by_ker(self):
#         self._draw_matrix(use_diff=False)

#     # ====================== ИСПРАВЛЕННЫЕ ВИЗУАЛИЗАЦИИ ======================

#     def show_spiral_2d(self):
#         self.canvas.delete("all")
#         w = self.canvas.winfo_width() or 800
#         h = self.canvas.winfo_height() or 600
#         cx, cy = w // 2, h // 2

#         conn = sqlite3.connect(self.db_path)
#         c = conn.cursor()
#         c.execute("SELECT ker FROM ker_diff ORDER BY x, y LIMIT 800")
#         data = [row[0] for row in c.fetchall()]
#         conn.close()

#         for i, ker in enumerate(data):
#             color = get_hmm_color(ker, self.model_var.get())
#             angle = i * 0.17
#             radius = min(w, h) * 0.38 * (0.08 + i / max(len(data), 1))
#             x = cx + radius * (angle ** 0.68)
#             y = cy + radius * 0.57
#             size = 6.5
#             self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")

#         self.canvas.config(scrollregion=(0, 0, w, h))

#     def show_gradient(self):
#         self.canvas.delete("all")
#         w = self.canvas.winfo_width() or 800
#         h = self.canvas.winfo_height() or 600
        
#         rows = 45
#         cols = 45
#         cell_w = w / cols
#         cell_h = h / rows

#         for i in range(rows):
#             for j in range(cols):
#                 value = i * 4 + j
#                 color = get_hmm_color(value, self.model_var.get(), max_val=180)
#                 self.canvas.create_rectangle(
#                     j * cell_w, i * cell_h,
#                     (j + 1) * cell_w, (i + 1) * cell_h,
#                     fill=color, 
#                     outline="#222222" if self.grid_var.get() else ""
#                 )

#         self.canvas.config(scrollregion=(0, 0, w, h))
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from data.hmm_models import get_hmm_color, get_model_legend_info


class Form2D(tk.Toplevel):
    def __init__(self, parent, db_path="hmm_data.db"):
        super().__init__(parent)
        self.db_path = db_path
        
        self.title("Объект 2D: Ker(|X² - Y²|)")
        self.geometry("1180x820")
        self.minsize(1000, 700)

        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        tk.Label(main_frame, text="Объект 2D: Ker(Разность квадратов чисел)", 
                font=("Arial", 16, "bold")).pack(pady=(0, 8))

        # ==================== ЛЕВАЯ ПАНЕЛЬ ====================
        left_frame = tk.Frame(main_frame, width=340)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
        left_frame.pack_propagate(False)

        param_frame = tk.LabelFrame(left_frame, text="Параметры моделирования", padx=12, pady=12)
        param_frame.pack(fill=tk.BOTH, expand=True)

        # Выбор модели
        tk.Label(param_frame, text="Модель НММ:").pack(anchor="w", pady=(0,4))
        self.model_var = tk.StringVar(value="НММ_Rainbow")
        self.model_combo = ttk.Combobox(param_frame, textvariable=self.model_var, 
                    values=["НММ_N", "НММ_N2", "НММ_Rainbow"], 
                    width=25, state="readonly")
        self.model_combo.pack(anchor="w", pady=4)

        # === УПРОЩЁННАЯ ЦВЕТОВАЯ ПАЛИТРА ===
        tk.Label(param_frame, text="Палитра модели:", font=("Arial", 10)).pack(anchor="w", pady=(6,2))
        
        self.legend_canvas = tk.Canvas(param_frame, height=26, bg="#1e1e1e", 
                                       highlightthickness=1, highlightbackground="#555")
        self.legend_canvas.pack(fill=tk.X, pady=(0, 10), padx=2)

        # Aspect
        tk.Label(param_frame, text="Aspect:").pack(anchor="w", pady=(2,4))
        self.aspect_var = tk.DoubleVar(value=1.0)
        tk.Entry(param_frame, textvariable=self.aspect_var, width=12).pack(anchor="w", pady=2)

        # Диапазоны
        range_f = tk.LabelFrame(param_frame, text="Диапазоны", padx=10, pady=8)
        range_f.pack(fill=tk.X, pady=10)
        
        tk.Label(range_f, text="Xmin:").grid(row=0, column=0, sticky="e", padx=4)
        self.xmin_var = tk.IntVar(value=1)
        tk.Entry(range_f, textvariable=self.xmin_var, width=8).grid(row=0, column=1, padx=4)
        
        tk.Label(range_f, text="Xmax:").grid(row=0, column=2, sticky="e", padx=4)
        self.xmax_var = tk.IntVar(value=50)
        tk.Entry(range_f, textvariable=self.xmax_var, width=8).grid(row=0, column=3, padx=4)

        tk.Label(range_f, text="Ymin:").grid(row=1, column=0, sticky="e", padx=4, pady=6)
        self.ymin_var = tk.IntVar(value=1)
        tk.Entry(range_f, textvariable=self.ymin_var, width=8).grid(row=1, column=1, padx=4)
        
        tk.Label(range_f, text="Ymax:").grid(row=1, column=2, sticky="e", padx=4, pady=6)
        self.ymax_var = tk.IntVar(value=50)
        tk.Entry(range_f, textvariable=self.ymax_var, width=8).grid(row=1, column=3, padx=4)

        tk.Label(param_frame, text="Опции:").pack(anchor="w", pady=(12,4))
        self.value_var = tk.BooleanVar(value=False)
        self.grid_var = tk.BooleanVar(value=True)
        tk.Checkbutton(param_frame, text="Value (значения)", variable=self.value_var).pack(anchor="w")
        tk.Checkbutton(param_frame, text="Grid (сетка)", variable=self.grid_var).pack(anchor="w")

        tk.Label(param_frame, text="Визуализация:").pack(anchor="w", pady=(15,4))
        self.vis_var = tk.StringVar(value="Цветная матрица")
        self.vis_combo = ttk.Combobox(param_frame, textvariable=self.vis_var,
                                     values=["Цветная матрица", "По Ker", "Спираль 2D", "Градиентная"],
                                     width=28, state="readonly")
        self.vis_combo.pack(anchor="w", pady=4)

        # Кнопки
        tk.Button(param_frame, text="Применить / Пересчитать", 
                  font=("Arial", 11, "bold"), 
                  command=self.apply_visualization).pack(fill=tk.X, pady=12)

        btn_frame = tk.Frame(param_frame)
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text="Справка", command=self.show_help).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        tk.Button(btn_frame, text="Закрыть", command=self.destroy).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # ==================== CANVAS ====================
        canvas_frame = tk.Frame(main_frame)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        v_scroll = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        h_scroll = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)

        self.canvas = tk.Canvas(canvas_frame, bg="#0a0a0a", highlightthickness=2,
                               highlightbackground="#555",
                               xscrollcommand=h_scroll.set,
                               yscrollcommand=v_scroll.set)

        v_scroll.config(command=self.canvas.yview)
        h_scroll.config(command=self.canvas.xview)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)

        # Привязки
        self.model_combo.bind("<<ComboboxSelected>>", lambda e: self.update_legend_panel())
        self.bind("<Configure>", self.on_resize)
        self.after(300, self.apply_visualization)

    # ====================== УПРОЩЁННАЯ ПАЛИТРА ======================
    def update_legend_panel(self):
        """Только цветовая полоса без текста и цифр"""
        self.legend_canvas.delete("all")
        model = self.model_var.get()
        mod = 120

        w = self.legend_canvas.winfo_width() or 300
        h = 26

        steps = 140
        step_w = w / steps

        for i in range(steps):
            val = int(i * mod / steps)
            if model == "НММ_N":
                color = get_hmm_color(val, "НММ_N", mod=mod)
            elif model == "НММ_N2":
                color = get_hmm_color(val, "НММ_N2", mod=mod)
            else:
                color = get_hmm_color(val, "НММ_Rainbow", max_val=mod)

            x = i * step_w
            self.legend_canvas.create_rectangle(x, 2, x + step_w + 1, h-2,
                                              fill=color, outline="", tags="bar")

    # ====================== ОСНОВНЫЕ МЕТОДЫ ======================
    def on_resize(self, event=None):
        if hasattr(self, 'current_vis'):
            self.after(50, self.update_legend_panel)
            self.after(150, self.apply_visualization)

    def apply_visualization(self):
        self.current_vis = self.vis_var.get()
        self.update_legend_panel()   # обновляем палитру
        
        if self.current_vis == "Цветная матрица":
            self.show_matrix()
        elif self.current_vis == "По Ker":
            self.show_by_ker()
        elif self.current_vis == "Спираль 2D":
            self.show_spiral_2d()
        elif self.current_vis == "Градиентная":
            self.show_gradient()

    # (Остальные методы визуализации без изменений)
    def _draw_matrix(self, use_diff=False):
        self.canvas.delete("all")
        xmin, xmax = self.xmin_var.get(), self.xmax_var.get()
        ymin, ymax = self.ymin_var.get(), self.ymax_var.get()
        
        cols = xmax - xmin + 1
        cell_w = 18
        cell_h = int(cell_w * self.aspect_var.get())

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        field = "diff" if use_diff else "ker"
        c.execute(f"SELECT x, y, {field} FROM ker_diff WHERE x BETWEEN ? AND ? AND y BETWEEN ? AND ?",
                  (xmin, xmax, ymin, ymax))

        for x, y, value in c.fetchall():
            color = get_hmm_color(value, self.model_var.get(), 
                                mod=9 if not use_diff else 120, 
                                max_val=9 if not use_diff else 1000)
            
            px1 = (x - xmin) * cell_w
            py1 = (y - ymin) * cell_h
            px2 = px1 + cell_w
            py2 = py1 + cell_h

            self.canvas.create_rectangle(px1, py1, px2, py2,
                                       fill=color, 
                                       outline="#222222" if self.grid_var.get() else "")

            if self.value_var.get() and cell_w >= 22:
                text = str(value) if value < 100 else "●"
                self.canvas.create_text((px1+px2)//2, (py1+py2)//2, 
                                      text=text, fill="white", font=("Consolas", 8, "bold"))

        conn.close()
        self.canvas.config(scrollregion=(0, 0, cols*cell_w, (ymax-ymin+1)*cell_h))

    def show_matrix(self):
        self._draw_matrix(use_diff=True)

    def show_by_ker(self):
        self._draw_matrix(use_diff=False)

    def show_spiral_2d(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width() or 800
        h = self.canvas.winfo_height() or 600
        cx, cy = w // 2, h // 2

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT ker FROM ker_diff ORDER BY x, y LIMIT 800")
        data = [row[0] for row in c.fetchall()]
        conn.close()

        for i, ker in enumerate(data):
            color = get_hmm_color(ker, self.model_var.get())
            angle = i * 0.17
            radius = min(w, h) * 0.38 * (0.08 + i / max(len(data), 1))
            x = cx + radius * (angle ** 0.68)
            y = cy + radius * 0.57
            size = 6
            self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")

        self.canvas.config(scrollregion=(0, 0, w, h))

    def show_gradient(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width() or 800
        h = self.canvas.winfo_height() or 600
        rows, cols = 45, 45
        cell_w = w / cols
        cell_h = h / rows

        for i in range(rows):
            for j in range(cols):
                value = i * 5 + j
                color = get_hmm_color(value, self.model_var.get(), max_val=200)
                self.canvas.create_rectangle(j*cell_w, i*cell_h, (j+1)*cell_w, (i+1)*cell_h,
                                           fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, w, h))

    def show_help(self):
        import webbrowser
        import os
        
        # Путь к help.html (основная справка по 2D визуализации)
        help_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'help', 'help.html')
        
        # Проверяем существование файла
        if os.path.exists(help_file):
            webbrowser.open('file:///' + os.path.abspath(help_file))
        else:
            # Пробуем найти в текущей директории
            help_file = os.path.join(os.path.dirname(__file__), 'help.html')
            if os.path.exists(help_file):
                webbrowser.open('file:///' + os.path.abspath(help_file))
            else:
                messagebox.showwarning("Файл не найден", 
                                    f"Файл help.html не найден.\n\nСоздайте файл справки в папке help/")

        tk.Button(help_win, text="Закрыть", command=help_win.destroy, 
                 font=("Arial", 10), width=12).pack(pady=10)