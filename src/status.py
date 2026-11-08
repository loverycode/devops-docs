def format_status(version: str, deployed: bool) -> str:
    """Возвращает человекочитаемое состояние публикации."""
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"
