import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3,os,webbrowser,math
from data.hmm_models import get_hmm_color, get_model_legend_info


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

        #left panel
        left_frame = tk.Frame(main_frame, width=340)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 12))
        left_frame.pack_propagate(False)

        param_frame = tk.LabelFrame(left_frame, text="Параметры моделирования", padx=12, pady=12)
        param_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(param_frame, text="Модель НММ:").pack(anchor="w", pady=(0,4))
        self.model_var = tk.StringVar(value="НММ_Rainbow")
        self.model_combo = ttk.Combobox(param_frame, textvariable=self.model_var, 
                    values=["НММ_N", "НММ_N2", "НММ_Rainbow"], 
                    width=25, state="readonly")
        self.model_combo.pack(anchor="w", pady=4)

        tk.Label(param_frame, text="Палитра модели:", font=("Arial", 10)).pack(anchor="w", pady=(6,2))
        
        self.legend_canvas = tk.Canvas(param_frame, height=26, bg="#1e1e1e", 
                                       highlightthickness=1, highlightbackground="#555")
        self.legend_canvas.pack(fill=tk.X, pady=(0, 10), padx=2)

        tk.Label(param_frame, text="Модуль (для визуализации):").pack(anchor="w", pady=(4,4))
        self.mod_var = tk.IntVar(value=100)
        tk.Entry(param_frame, textvariable=self.mod_var, width=15).pack(anchor="w", pady=2)

        tk.Label(param_frame, text="Количество элементов:").pack(anchor="w", pady=(8,4))
        self.count_var = tk.IntVar(value=100)
        tk.Entry(param_frame, textvariable=self.count_var, width=15).pack(anchor="w", pady=2)

        tk.Label(param_frame, text="Опции:").pack(anchor="w", pady=(12,4))
        self.grid_var = tk.BooleanVar(value=True)
        tk.Checkbutton(param_frame, text="Grid (сетка)", variable=self.grid_var).pack(anchor="w")

        tk.Label(param_frame, text="Визуализация:").pack(anchor="w", pady=(15,4))
        self.vis_var = tk.StringVar(value="Линейная")
        self.vis_combo = ttk.Combobox(param_frame, textvariable=self.vis_var,
                                     values=["Линейная", "Столбчатая", "Спираль", "Мозаика"],
                                     width=28, state="readonly")
        self.vis_combo.pack(anchor="w", pady=4)

        tk.Button(param_frame, text="Применить / Пересчитать", 
                  font=("Arial", 11, "bold"), 
                  command=self.apply_visualization).pack(fill=tk.X, pady=12)

        btn_frame = tk.Frame(param_frame)
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text="Справка", command=self.show_help).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        tk.Button(btn_frame, text="Закрыть", command=self.destroy).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        #canvas
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

        self.model_combo.bind("<<ComboboxSelected>>", lambda e: self.update_legend_panel())
        self.bind("<Configure>", self.on_resize)
        self.after(300, self.apply_visualization)

    def update_legend_panel(self):
        self.legend_canvas.delete("all")
        model = self.model_var.get()
        mod = self.mod_var.get() if self.mod_var.get() > 0 else 100

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

    #methods
    def on_resize(self, event=None):
        if hasattr(self, 'current_vis'):
            self.after(50, self.update_legend_panel)
            self.after(150, self.apply_visualization)

    def apply_visualization(self):
        self.current_vis = self.vis_var.get()
        self.update_legend_panel()   # обновляем палитру
        
        if self.current_vis == "Линейная":
            self.show_linear()
        elif self.current_vis == "Столбчатая":
            self.show_bars()
        elif self.current_vis == "Спираль":
            self.show_spiral()
        elif self.current_vis == "Мозаика":
            self.show_mosaic()

    def get_fib_data(self, limit=500):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute("SELECT value FROM fib ORDER BY n LIMIT ?", (limit,))
            data = [row[0] for row in c.fetchall()]
            conn.close()
            return data if data else [0, 1, 1, 2, 3, 5]
        except:
            from source.utils import fib_mod_sequence
            return fib_mod_sequence(limit, self.mod_var.get())

    # ====================== ВИЗУАЛИЗАЦИИ ======================
    def show_linear(self):
        self.canvas.delete("all")
        data = self.get_fib_data(self.count_var.get())
        cell_w = 18
        total_w = len(data) * cell_w

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            x1 = i * cell_w
            self.canvas.create_rectangle(x1, 30, x1 + cell_w, 520, 
                                       fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, total_w, 600))

    def show_bars(self):
        self.canvas.delete("all")
        data = self.get_fib_data(min(self.count_var.get(), 400))
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

    # def show_spiral(self):
    #     self.canvas.delete("all")
    #     data = self.get_fib_data(self.count_var.get())
    #     w = self.canvas.winfo_width() or 800
    #     h = self.canvas.winfo_height() or 600
    #     cx, cy = w // 2, h // 2

    #     for i, v in enumerate(data):
    #         color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
    #         angle = i * 0.16
    #         radius = min(w, h) * 0.37 * (0.1 + i / len(data))
    #         x = cx + radius * (angle ** 0.7)
    #         y = cy + radius * 0.55
    #         size = 6.5
    #         self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")

    #     self.canvas.config(scrollregion=(0, 0, w, h))

    def show_spiral(self):
        self.canvas.delete("all")

        data = self.get_fib_data(self.count_var.get())

        w = self.canvas.winfo_width() or 900
        h = self.canvas.winfo_height() or 700

        cx, cy = w // 2, h // 2

        max_radius = min(w, h) * 0.42

        for i, v in enumerate(data):

            color = get_hmm_color(
                v,
                self.model_var.get(),
                self.mod_var.get()
            )

            # угол
            angle = i * 0.32

            # радиус
            radius = max_radius * (i / len(data))

            # координаты спирали
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)

            # размер точки зависит от значения
            size = 4 + (v % 7)

            self.canvas.create_oval(
                x - size,
                y - size,
                x + size,
                y + size,
                fill=color,
                outline=""
            )

        self.canvas.config(scrollregion=(0, 0, w, h))
    def show_mosaic(self):
        self.canvas.delete("all")
        data = self.get_fib_data(self.count_var.get())
        cell_size = 22
        cols = 40
        total_w = cols * cell_size
        total_h = ((len(data) // cols) + 3) * cell_size

        for i, v in enumerate(data):
            color = get_hmm_color(v, self.model_var.get(), self.mod_var.get())
            x = (i % cols) * cell_size
            y = (i // cols) * cell_size
            self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size,
                                       fill=color, outline="#222" if self.grid_var.get() else "")

        self.canvas.config(scrollregion=(0, 0, total_w, total_h))

    def show_help(self):
        help_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'help', 'help.html')
        if os.path.exists(help_file):
            webbrowser.open('file:///' + os.path.abspath(help_file))
        # else:
        #     help_file = os.path.join(os.path.dirname(__file__), 'help.html')
        #     if os.path.exists(help_file):
        #         webbrowser.open('file:///' + os.path.abspath(help_file))
        #     else:
        #         messagebox.showwarning("Файл не найден", 
        #                             f"Файл help_keys.html не найден.\n\nСоздайте файл справки в папке help/")

        tk.Button(help_win, text="Закрыть", command=help_win.destroy, 
                 font=("Arial", 10), width=12).pack(pady=10)