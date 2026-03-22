def add(a: float, b: float) -> float:
    """Retourne la somme de a et b.

    Raises:
        TypeError: Si a ou b ne sont pas des nombres.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Opérandes invalides : {type(a)}, {type(b)}")
    return a - b


def divide(a: float, b: float) -> float:
    """Divise a par b.

    Raises:
        ValueError: Si b == 0.
        TypeError: Si a ou b ne sont pas des nombres.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Opérandes invalides : {type(a)}, {type(b)}")
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b