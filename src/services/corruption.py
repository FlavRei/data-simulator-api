import random

def corrupt_value(value: str):
    """Ajoute des erreurs typiques (fautes, valeurs manquantes, etc.)"""
    if value is None:
        return None
    r = random.random()
    # 8% -> None
    if r < 0.08:
        return None
    # 8% -> lowercase
    if r < 0.16 and isinstance(value, str):
        return value.lower()
    # 4% -> reversed
    if r < 0.20 and isinstance(value, str):
        return value[::-1]
    # 4% -> empty string
    if r < 0.24:
        return ""
    # 3% -> add typo (swap two chars)
    if r < 0.27 and isinstance(value, str) and len(value) > 3:
        i = random.randint(0, len(value)-2)
        lst = list(value)
        lst[i], lst[i+1] = lst[i+1], lst[i]
        return "".join(lst)
    return value
