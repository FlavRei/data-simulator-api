import random

def corrupt_value(value: str):
    """Ajoute des erreurs typiques (fautes, valeurs manquantes, etc.)"""
    if value is None:
        return None
    r = random.random()
    # 6% -> None
    if r < 0.06:
        return None
    # 4% -> lowercase
    if r < 0.10 and isinstance(value, str):
        return value.lower()
    # 2% -> reversed
    if r < 0.12 and isinstance(value, str):
        return value[::-1]
    # 6% -> empty string
    if r < 0.18:
        return ""
    # 2% -> add typo (swap two chars)
    if r < 0.20 and isinstance(value, str) and len(value) > 3:
        i = random.randint(0, len(value)-2)
        lst = list(value)
        lst[i], lst[i+1] = lst[i+1], lst[i]
        return "".join(lst)
    return value
