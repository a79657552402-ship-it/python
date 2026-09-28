class NotValidError(Exception):
    """Исключение для невалидных данных (не список, пустой список и т.п.)."""

    def __init__(self, message="Невалидные данные", value=None):
        self.value = value
        super().__init__(f"{message}: {value!r}" if value is not None else message)