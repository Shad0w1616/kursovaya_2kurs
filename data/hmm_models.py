# import colorsys

# def get_hmm_color(value: int, model: str = "НММ_Rainbow", mod: int = 10, max_val: int = 100):
#     """Основной модуль хромоматематических моделей"""
    
#     value = value % mod if mod > 0 else value
    
#     if model == "НММ_N":
#         # Классическая монохромная: оттенки одного цвета (от тёмного к светлому)
#         intensity = value / (mod - 1) if mod > 1 else 0.5
#         # Можно выбрать базовый цвет (0.0 = красный, 0.6 = синий, 0.3 = зелёный и т.д.)
#         r, g, b = colorsys.hsv_to_rgb(0.0, 0.0, intensity)        # чистый grayscale
#         # r, g, b = colorsys.hsv_to_rgb(0.65, 0.85, intensity)    # синие тона (красивее)

#     elif model == "НММ_N2":
#         # Модифицированная — чаще всего два цвета или с изменением насыщенности
#         intensity = value / (mod - 1) if mod > 1 else 0.5
#         sat = 0.9 if value % 2 == 0 else 0.4
#         hue = 0.65 if value % 2 == 0 else 0.55          # можно два близких оттенка
#         r, g, b = colorsys.hsv_to_rgb(hue, sat, 0.95)

#     elif model == "НММ_Rainbow" or model == "НММ_R":
#         # Полноцветная радуга
#         hue = (value % max_val) / max_val
#         r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.95)

#     else:
#         return "#555555"

#     return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
# import colorsys

# def get_hmm_color(value: int, model: str = "НММ_Rainbow", mod: int = 10, max_val: int = 100):
#     """Основной модуль хромоматематических моделей"""
#     value = int(value)
#     if mod > 0:
#         value = value % mod

#     if model == "НММ_N":
#         # Монохромная модель — оттенки одного цвета (серый)
#         intensity = value / (mod - 1) if mod > 1 else 0.5
#         r, g, b = colorsys.hsv_to_rgb(0.0, 0.0, intensity)  # grayscale

#     elif model == "НММ_N2":
#         # Модифицированная монохромная (двухцветный градиент)
#         t = value / (mod - 1) if mod > 1 else 0.5
#         hue = 0.58 + t * 0.25          # от синего к пурпурно-красному
#         sat = 0.75 + t * 0.25
#         r, g, b = colorsys.hsv_to_rgb(hue, sat, 0.96)

#     elif model in ["НММ_Rainbow", "НММ_R"]:
#         # Полноцветная радуга
#         hue = (value % max_val) / max_val
#         r, g, b = colorsys.hsv_to_rgb(hue, 0.92, 0.96)

#     else:
#         return "#555555"

#     return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
import colorsys

def get_hmm_color(value: int, model: str = "НММ_Rainbow", mod: int = 10, max_val: int = 100):
    """Основной модуль хромоматематических моделей"""
    value = int(value)

    if model == "НММ_N":
        # Монохромная
        value = value % mod if mod > 1 else value
        intensity = value / (mod - 1) if mod > 1 else 0.5
        r, g, b = colorsys.hsv_to_rgb(0.0, 0.0, intensity)

    elif model == "НММ_N2":
        # Модифицированная
        value = value % mod if mod > 1 else value
        t = value / (mod - 1) if mod > 1 else 0.5
        hue = 0.58 + t * 0.25
        sat = 0.75 + t * 0.25
        r, g, b = colorsys.hsv_to_rgb(hue, sat, 0.96)

    elif model in ["НММ_Rainbow", "НММ_R"]:
        # Rainbow — ПОЛНЫЙ спектр, без mod!
        hue = (value % max_val) / max_val
        r, g, b = colorsys.hsv_to_rgb(hue, 0.92, 0.96)

    else:
        return "#555555"

    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

def get_model_legend_info(model: str, mod: int = 100):
    """Информация для легенды"""
    if model == "НММ_N":
        return {"type": "mono", "name": "НММ_N — Монохромоматематическая по модулю N", "mod": mod}
    elif model == "НММ_N2":
        return {"type": "bi", "name": "НММ_N2 — Монохромоматематическая 2 (модифицированная)", "mod": mod}
    elif model in ["НММ_Rainbow", "НММ_R"]:
        return {"type": "rainbow", "name": "НММ_Rainbow — Мультиградиентная (радуга)", "mod": mod}
    return {"type": "unknown", "name": model, "mod": mod}