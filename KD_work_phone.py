import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

#Сделали просто отдельные типы ошибок, чтоб различать могли
class PhoneNumberError(Exception):
    pass

class InvalidStartError(PhoneNumberError):
    pass

class InvalidBracketsError(PhoneNumberError):
    pass

class InvalidDashError(PhoneNumberError):
    pass

class InvalidDigitCountError(PhoneNumberError):
    pass

class InvalidCharacterError(PhoneNumberError):
    pass

def normalize_phone(phone):

    if any(char.isalpha() for char in phone):
        raise InvalidCharacterError(
            "Номер не должен содержать буквы."
        )

    for char in phone:
        if not (
            char in "0123456789"
            or char.isspace()
            or char in "+()-"
        ):
            raise InvalidCharacterError(
                "Номер содержит недопустимые символы."
            )

    compact = "".join(phone.split())

    if not (compact.startswith("+7") or compact.startswith("8")):
        raise InvalidStartError(
            "Номер должен начинаться с +7 или 8."
        )

    left = compact.count("(")
    right = compact.count(")")

    if left > 1 or right > 1:
        raise InvalidBracketsError(
            "Допускается только одна пара скобок."
        )

    if left != right:
        raise InvalidBracketsError(
            "Количество открывающих и закрывающих скобок не совпадает."
        )

    if left == 1:
        if compact.index("(") > compact.index(")"):
            raise InvalidBracketsError(
                "Закрывающая скобка не может стоять раньше открывающей."
            )

    if (
        compact.startswith("-")
        or compact.endswith("-")
        or "--" in compact
    ):
        raise InvalidDashError(
            "Дефисы не могут стоять в начале, конце или подряд."
        )

    if compact.startswith("+7"):
        if compact.count("+") != 1:
            raise InvalidCharacterError(
                "Знак + должен стоять только в начале номера."
            )
    elif "+" in compact:
        raise InvalidCharacterError(
            "Знак + должен стоять только в начале номера."
        )

    digits = "".join(
        char for char in compact if char in "0123456789"
    )

    if len(digits) != 11:
        raise InvalidDigitCountError(
            "Номер должен содержать ровно 11 цифр."
        )

    try:
        if digits[0] == "8":
            result = "+7" + digits[1:]
        else:
            result = "+" + digits

    except (IndexError, TypeError, ValueError) as error:
        raise PhoneNumberError(
            f"Ошибка преобразования номера: {error}"
        ) from error

    return result

class PhoneWindowKDO(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Проверка телефонного номера")
        self.resize(450, 190)

        layout = QVBoxLayout()

        self.title = QLabel("Введите номер телефона:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("+7 905 343-43-41")

        self.check_button = QPushButton("Проверить номер")

        self.status_label = QLabel("")
        self.status_label.setMinimumHeight(35)
        self.status_label.setWordWrap(True)

        layout.addWidget(self.title)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.check_button.clicked.connect(self.check_phone_KDO)
        self.phone_input.returnPressed.connect(self.check_phone_KDO)
        self.phone_input.textChanged.connect(self.clear_status_KDO)

    def check_phone_KDO(self):

        phone = self.phone_input.text()

        try:
            result = normalize_phone(phone)

            self.status_label.setText(
                f"Номер успешно введён: {result}"
            )
            self.status_label.setStyleSheet(
                "color: green; font-weight: bold;"
            )

        except PhoneNumberError as error:

            self.status_label.setText(
                f"Ошибка: {error}")
            self.status_label.setStyleSheet(
                "color: red; font-weight: bold;"
            )

    def clear_status_KDO(self):
        self.status_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneWindowKDO()
    window.show()
    sys.exit(app.exec())