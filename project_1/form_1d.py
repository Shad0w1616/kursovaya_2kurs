# import tkinter as tk
# from tkinter import ttk
# from utils import fib_mod_sequence
# from hmm_models import get_hmm_color

# class Form1D(tk.Toplevel):
#     def __init__(self, parent, db_path="hmm_data.db"):
#         super().__init__(parent)
#         self.db_path = db_path
#         self.title("Объект 1D: Числа Фибоначчи по модулю")
#         self.geometry("1180x780")
#         self.minsize(1000, 680)

#         # ... (весь интерфейс остаётся тем же) ...

#         main_frame = tk.Frame(self)
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

#         tk.Label(main_frame, text="Объект 1D: Числа Фибоначчи по модулю", 
#                 font=("Arial", 16, "bold")).pack(pady=(0, 8))

#         # Левая панель параметров (без изменений)
#         left_frame = tk.Frame(main_frame, width=340)
#         left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
#         left_frame.pack_propagate(False)

#         param_frame = tk.LabelFrame(left_frame, text="Параметры моделирования", padx=12, pady=12)
#         param_frame.pack(fill=tk.BOTH, expand=True)

#         tk.Label(param_frame, text="Модель НММ:").pack(anchor="w", pady=(0,4))
#         self.model_var = tk.StringVar(value="НММ_Rainbow")
#         ttk.Combobox(param_frame, textvariable=self.model_var, 
#                     values=["НММ_N", "НММ_N2", "НММ_Rainbow"], 
#                     width=25, state="readonly").pack(anchor="w", pady=4)

#         tk.Label(param_frame, text="Модуль:").pack(anchor="w", pady=(8,4))
#         self.mod_var = tk.IntVar(value=100)
#         tk.Entry(param_frame, textvariable=self.mod_var, width=15).pack(anchor="w", pady=4)

#         tk.Label(param_frame, text="Количество элементов:").pack(anchor="w", pady=(12,4))
#         self.count_var = tk.IntVar(value=400)
#         tk.Entry(param_frame, textvariable=self.count_var, width=15).pack(anchor="w", pady=4)

#         tk.Label(param_frame, text="Опции:").pack(anchor="w", pady=(15,4))
#         self.grid_var = tk.BooleanVar(value=True)
#         tk.Checkbutton(param_frame, text="Grid (сетка)", variable=self.grid_var).pack(anchor="w")

#         tk.Label(param_frame, text="Визуализация:").pack(anchor="w", pady=(15,4))
#         self.vis_var = tk.StringVar(value="Линейная")
#         self.vis_combo = ttk.Combobox(param_frame, textvariable=self.vis_var,
#                                      values=["Линейная", "Столбчатая", "Спираль", "Мозаика"],
#                                      width=28, state="readonly")
#         self.vis_combo.pack(anchor="w", pady=4)

#         tk.Button(param_frame, text="Применить / Пересчитать", 
#                  font=("Arial", 11, "bold"), command=self.apply_visualization).pack(fill=tk.X, pady=12)

#         # Canvas со скроллом
#         canvas_frame = tk.Frame(main_frame)
#         canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

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
#         self.after(250, self.apply_visualization)

#     def on_resize(self, event=None):
#         if hasattr(self, 'current_vis'):
#             self.after(100, self.apply_visualization)

#     def apply_visualization(self):
#         self.current_vis = self.vis_var.get()
#         if self.current_vis == "Линейная":
#             self.show_linear()
#         elif self.current_vis == "Столбчатая":
#             self.show_bars()
#         elif self.current_vis == "Спираль":
#             self.show_spiral()
#         elif self.current_vis == "Мозаика":
#             self.show_mosaic()

#     # ====================== ВИЗУАЛИЗАЦИИ 1D ======================

#     def show_linear(self):
#         self.canvas.delete("all")
#         data = fib_mod_sequence(self.count_var.get(), self.mod_var.get())
#         cell_w = 18
#         total_w = len(data) * cell_w

#         for i, v in enumerate(data):
#             color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
#             x1 = i * cell_w
#             self.canvas.create_rectangle(x1, 30, x1 + cell_w, 550, 
#                                        fill=color, outline="#222" if self.grid_var.get() else "")

#         self.canvas.config(scrollregion=(0, 0, total_w, 600))

#     def show_bars(self):
#         self.canvas.delete("all")
#         data = fib_mod_sequence(min(self.count_var.get(), 300), self.mod_var.get())
#         if not data: return
#         max_v = max(data)
#         cell_w = 12
#         total_w = len(data) * cell_w

#         for i, v in enumerate(data):
#             color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
#             height = int(480 * (v / max_v))
#             x1 = i * cell_w
#             self.canvas.create_rectangle(x1, 550 - height, x1 + cell_w, 550,
#                                        fill=color, outline="#222" if self.grid_var.get() else "")

#         self.canvas.config(scrollregion=(0, 0, total_w, 600))

#     def show_spiral(self):
#         self.canvas.delete("all")
#         data = fib_mod_sequence(self.count_var.get(), self.mod_var.get())
#         w = self.canvas.winfo_width() or 800
#         h = self.canvas.winfo_height() or 600
#         cx, cy = w // 2, h // 2

#         for i, v in enumerate(data):
#             color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
#             angle = i * 0.16
#             radius = min(w, h) * 0.37 * (0.1 + i / len(data))
#             x = cx + radius * (angle ** 0.7)
#             y = cy + radius * 0.55
#             size = 6
#             self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")

#         self.canvas.config(scrollregion=(0, 0, w, h))

#     def show_mosaic(self):
#         self.canvas.delete("all")
#         data = fib_mod_sequence(self.count_var.get(), self.mod_var.get())
#         cell_size = 22
#         cols = 35
#         total_w = cols * cell_size
#         total_h = ((len(data) // cols) + 1) * cell_size

#         for i, v in enumerate(data):
#             color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
#             x = (i % cols) * cell_size
#             y = (i // cols) * cell_size
#             self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size,
#                                        fill=color, outline="#222" if self.grid_var.get() else "")

#         self.canvas.config(scrollregion=(0, 0, total_w, total_h))
import tkinter as tk
from tkinter import ttk
import sqlite3
from hmm_models import get_hmm_color


class Form1D(tk.Toplevel):
    def __init__(self, parent, db_path="hmm_data.db"):
        super().__init__(parent)
        self.db_path = db_path
        
        self.title("Объект 1D: Числа Фибоначчи по модулю")
        self.geometry("1180x780")
        self.minsize(1000, 680)

        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        tk.Label(main_frame, text="Объект 1D: Числа Фибоначчи по модулю", 
                font=("Arial", 16, "bold")).pack(pady=(0, 8))

        # Левая панель
        left_frame = tk.Frame(main_frame, width=340)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
        left_frame.pack_propagate(False)

        param_frame = tk.LabelFrame(left_frame, text="Параметры моделирования", padx=12, pady=12)
        param_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(param_frame, text="Модель НММ:").pack(anchor="w", pady=(0,4))
        self.model_var = tk.StringVar(value="НММ_Rainbow")
        ttk.Combobox(param_frame, textvariable=self.model_var, 
                    values=["НММ_N", "НММ_N2", "НММ_Rainbow"], 
                    width=25, state="readonly").pack(anchor="w", pady=4)

        tk.Label(param_frame, text="Модуль (для визуализации):").pack(anchor="w", pady=(8,4))
        self.mod_var = tk.IntVar(value=100)
        tk.Entry(param_frame, textvariable=self.mod_var, width=15).pack(anchor="w", pady=4)

        tk.Label(param_frame, text="Количество элементов:").pack(anchor="w", pady=(12,4))
        self.count_var = tk.IntVar(value=500)
        tk.Entry(param_frame, textvariable=self.count_var, width=15).pack(anchor="w", pady=4)

        tk.Label(param_frame, text="Опции:").pack(anchor="w", pady=(15,4))
        self.grid_var = tk.BooleanVar(value=True)
        tk.Checkbutton(param_frame, text="Grid (сетка)", variable=self.grid_var).pack(anchor="w")

        tk.Label(param_frame, text="Визуализация:").pack(anchor="w", pady=(15,4))
        self.vis_var = tk.StringVar(value="Линейная")
        self.vis_combo = ttk.Combobox(param_frame, textvariable=self.vis_var,
                                     values=["Линейная", "Столбчатая", "Спираль", "Мозаика"],
                                     width=28, state="readonly")
        self.vis_combo.pack(anchor="w", pady=4)

        # ====================== КНОПКИ ======================
        # Кнопка Применить
        apply_btn_frame = tk.Frame(param_frame)
        apply_btn_frame.pack(fill=tk.X, pady=(12, 6))
        
        tk.Button(apply_btn_frame, text="Применить / Пересчитать", 
                  font=("Arial", 11, "bold"), 
                  command=self.apply_visualization).pack(fill=tk.X, padx=2)

        # Кнопки Справка и Закрыть ниже
        btn_frame = tk.Frame(param_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 12))

        tk.Button(btn_frame, text="Справка", 
                  font=("Arial", 10, "bold"), 
                  command=self.show_help).pack(side=tk.LEFT, padx=(0, 8), fill=tk.X, expand=True)

        tk.Button(btn_frame, text="Закрыть", 
                  font=("Arial", 10, "bold"), 
                  command=self.destroy).pack(side=tk.LEFT, padx=(0, 0), fill=tk.X, expand=True)

        # ==================== Canvas ====================
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

        self.bind("<Configure>", self.on_resize)
        self.after(300, self.apply_visualization)

    def on_resize(self, event=None):
        if hasattr(self, 'current_vis'):
            self.after(100, self.apply_visualization)

    def apply_visualization(self):
        self.current_vis = self.vis_var.get()
        if self.current_vis == "Линейная":
            self.show_linear()
        elif self.current_vis == "Столбчатая":
            self.show_bars()
        elif self.current_vis == "Спираль":
            self.show_spiral()
        elif self.current_vis == "Мозаика":
            self.show_mosaic()

    # ====================== РАБОТА С БД ======================
    def _get_fib_data(self, limit=500):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute("SELECT value FROM fib ORDER BY n LIMIT ?", (limit,))
            data = [row[0] for row in c.fetchall()]
            conn.close()
            return data if data else [0, 1, 1, 2, 3, 5]
        except:
            from utils import fib_mod_sequence
            return fib_mod_sequence(limit, self.mod_var.get())

    # ====================== ВИЗУАЛИЗАЦИИ ======================
    def show_linear(self):
        self.canvas.delete("all")
        data = self._get_fib_data(self.count_var.get())
        cell_w = 18
        total_w = len(data) * cell_w

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            x1 = i * cell_w
            self.canvas.create_rectangle(x1, 30, x1 + cell_w, 550, 
                                       fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, total_w, 600))

    def show_bars(self):
        self.canvas.delete("all")
        data = self._get_fib_data(min(self.count_var.get(), 400))
        if not data: return
        max_v = max(data) or 1
        cell_w = 12
        total_w = len(data) * cell_w

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            height = int(480 * (v / max_v))
            x1 = i * cell_w
            self.canvas.create_rectangle(x1, 550 - height, x1 + cell_w, 550,
                                       fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, total_w, 600))

    def show_spiral(self):
        self.canvas.delete("all")
        data = self._get_fib_data(self.count_var.get())
        w = self.canvas.winfo_width() or 800
        h = self.canvas.winfo_height() or 600
        cx, cy = w // 2, h // 2

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            angle = i * 0.16
            radius = min(w, h) * 0.37 * (0.1 + i / len(data))
            x = cx + radius * (angle ** 0.7)
            y = cy + radius * 0.55
            size = 6.5
            self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")

        self.canvas.config(scrollregion=(0, 0, w, h))

    def show_mosaic(self):
        self.canvas.delete("all")
        data = self._get_fib_data(self.count_var.get())
        cell_size = 22
        cols = 35
        total_w = cols * cell_size
        total_h = ((len(data) // cols) + 2) * cell_size

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            x = (i % cols) * cell_size
            y = (i // cols) * cell_size
            self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size,
                                       fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, total_w, total_h))

    # ====================== СПРАВКА ======================
    def show_help(self):
        help_win = tk.Toplevel(self)
        help_win.title("Справка — Объект 1D")
        help_win.geometry("580x520")
        help_win.resizable(False, False)

        text = tk.Text(help_win, wrap=tk.WORD, padx=15, pady=15, font=("Consolas", 10))
        text.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(help_win, command=text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=scrollbar.set)

        help_text = """Объект 1D: Числа Фибоначчи по модулю

Основные возможности:
- Модель НММ — выбор цветовой схемы (Rainbow, N, N2)
- Модуль — по какому числу берётся остаток Фибоначчи
- Количество элементов — длина последовательности

Визуализации:
- Линейная — горизонтальная лента ячеек
- Столбчатая — гистограмма высотой пропорционально значению
- Спираль — спиральная раскладка точек
- Мозаика — табличное представление

Сетка и другие опции включаются в левой панели."""
        
        text.insert("1.0", help_text)
        text.config(state=tk.DISABLED)

        tk.Button(help_win, text="Закрыть", command=help_win.destroy, 
                 font=("Arial", 10), width=12).pack(pady=10)