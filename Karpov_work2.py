import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout

# Класс главного окна приложения
class WordsKDO(QWidget):

    def __init__(self):
        super().__init__()

        # Создаём интерфейс
        self.InitUI()

    # Метод для создания элементов интерфейса
    def InitUI(self):
        self.setWindowTitle("Перемещение текста KDO")
        self.resize(450, 100)

        # Создаём первое текстовое поле
        self.value_1 = QLineEdit()
        self.value_1.setObjectName("value_1")

        # Создаём второе текстовое поле
        self.value_2 = QLineEdit()
        self.value_2.setObjectName("value_2")

        # Создаём кнопку со стрелкой вправо
        self.arrow_button = QPushButton("->")
        self.arrow_button.setObjectName("arrow_button")

        # Создаём горизонтальную компоновку
        layout = QHBoxLayout()

        # Добавляем элементы в окно
        layout.addWidget(self.value_1)
        layout.addWidget(self.arrow_button)
        layout.addWidget(self.value_2)

        self.setLayout(layout)

        # Подключаем нажатие кнопки к обработчику
        self.arrow_button.clicked.connect(self.transfer_XXX)

    # Обработчик перемещения текста
    def transfer_KDO(self):

        # Проверяем направление стрелки
        if self.arrow_button.text() == "->":

            # Получаем текст из левого поля
            text = self.value_1.text()

            # Перемещаем текст в правое поле
            self.value_2.setText(text)

            # Очищаем левое поле
            self.value_1.clear()

            # Меняем направление стрелки
            self.arrow_button.setText("<-")

        else:

            # Получаем текст из правого поля
            text = self.value_2.text()

            # Перемещаем текст в левое поле
            self.value_1.setText(text)

            # Очищаем правое поле
            self.value_2.clear()

            # Возвращаем стрелку вправо
            self.arrow_button.setText("->")

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WordsKDO()
    window.show()

    sys.exit(app.exec())