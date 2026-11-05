import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)

# Пользовательское исключение для пустого поля
class EmptyFieldError(Exception):
    pass

# Класс главного окна приложения
class WordsKDO(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    # Создание интерфейса
    def InitUI(self):
        self.setWindowTitle("Перемещение текста")
        self.resize(450, 100)

        # Создаём первое текстовое поле
        self.value_1 = QLineEdit()
        self.value_1.setObjectName("value_1")

        # Создаём второе текстовое поле
        self.value_2 = QLineEdit()
        self.value_2.setObjectName("value_2")

        # Создаём кнопку со стрелкой
        self.arrow_button = QPushButton("->")
        self.arrow_button.setObjectName("arrow_button")

        # Размещаем элементы горизонтально
        layout = QHBoxLayout()
        layout.addWidget(self.value_1)
        layout.addWidget(self.arrow_button)
        layout.addWidget(self.value_2)
        self.setLayout(layout)

        # Подключаем кнопку к обработчику
        self.arrow_button.clicked.connect(self.transfer_KDO)

    # Обработчик перемещения текста
    def transfer_KDO(self):

        try:
            # Определяем направление перемещения
            if self.arrow_button.text() == "->":
                source = self.value_1
                target = self.value_2
                field_name = "слева"
            else:
                source = self.value_2
                target = self.value_1
                field_name = "справа"

            # Получаем текст из исходного поля
            text = source.text()

            # Удаляем пробелы по краям для проверки
            if not text.strip():
                raise EmptyFieldError(
                    f"Поле {field_name} пустое. "
                    "Текст не будет перемещён."
                )

            # Перемещаем текст
            target.setText(text)
            source.clear()

            # Меняем направление стрелки
            if self.arrow_button.text() == "->":
                self.arrow_button.setText("<-")
            else:
                self.arrow_button.setText("->")

        except EmptyFieldError as error:
            # Показываем сообщение об ошибке
            QMessageBox.warning(
                self,
                "Ошибка перемещения",
                str(error)
            )

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WordsKDO()
    window.show()
    sys.exit(app.exec())