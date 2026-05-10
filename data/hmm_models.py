import colorsys

def get_hmm_color(value: int, model: str = "НММ_Rainbow", mod: int = 10, max_val: int = 100):
    """Основной модуль хромоматематических моделей"""
    value = int(value)

    if model == "НММ_N":
        value = value % mod if mod > 1 else value
        intensity = value / (mod - 1) if mod > 1 else 0.5
        r, g, b = colorsys.hsv_to_rgb(0.0, 0.0, intensity)

    elif model == "НММ_N2":
        value = value % mod if mod > 1 else value
        t = value / (mod - 1) if mod > 1 else 0.5
        hue = 0.58 + t * 0.25
        sat = 0.75 + t * 0.25
        r, g, b = colorsys.hsv_to_rgb(hue, sat, 0.96)

    elif model in ["НММ_Rainbow", "НММ_R"]:
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