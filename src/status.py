def format_status(version: str, deployed: bool) -> str:
    """Возвращает человекочитаемое состояние публикации."""
    details = "temporary"  # <--- ВОТ ОНА, ОШИБКА PYLINT
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"
