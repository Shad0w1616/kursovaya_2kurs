import colorsys

def get_hmm_color(value: int, model: str = "НММ_Rainbow", mod: int = 10, max_val: int = 100) -> str:
    """Основной модуль хромоматематических моделей"""
    if model == "НММ_N":
        hue = (value % mod) / mod
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.95)
    elif model == "НММ_N2":
        hue = (value % mod) / mod
        sat = 1.0 if value % 2 == 0 else 0.55
        r, g, b = colorsys.hsv_to_rgb(hue, sat, 0.95)
    elif model == "НММ_Rainbow":
        hue = (value % max_val) / max_val
        r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.95)
    else:
        return "#555555"
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"