import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QLabel, QCheckBox, QGridLayout)
from PyQt6.QtCore import Qt

# Класс главного окна
class WidgetsKDO(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    # Создание интерфейса
    def InitUI(self):
        self.setWindowTitle("Управление видимостью виджетов")
        self.resize(500, 300)

        # Создаём два поля ввода
        self.value_1 = QLineEdit()
        self.value_1.setPlaceholderText("Поле ввода 1")

        self.value_2 = QLineEdit()
        self.value_2.setPlaceholderText("Поле ввода 2")

        # Создаём две кнопки
        self.button_1 = QPushButton("Кнопка 1")
        self.button_2 = QPushButton("Кнопка 2")

        # Создаём две надписи
        self.label_1 = QLabel("Надпись 1")
        self.label_2 = QLabel("Надпись 2")

        # Создаём шесть чекбоксов
        self.check_1 = QCheckBox("Поле ввода 1")
        self.check_2 = QCheckBox("Поле ввода 2")
        self.check_3 = QCheckBox("Кнопка 1")
        self.check_4 = QCheckBox("Кнопка 2")
        self.check_5 = QCheckBox("Надпись 1")
        self.check_6 = QCheckBox("Надпись 2")

        # Для первого чекбокса включаем три состояния:
        # Checked, Unchecked и PartiallyChecked
        self.check_1.setTristate(True)

        # Связываем каждый чекбокс с соответствующим виджетом
        self.widgets = {
            self.check_1: self.value_1,
            self.check_2: self.value_2,
            self.check_3: self.button_1,
            self.check_4: self.button_2,
            self.check_5: self.label_1,
            self.check_6: self.label_2
        }

        # При запуске все чекбоксы отмечены
        for check in self.widgets:
            check.setChecked(True)

            # Подключаем все чекбоксы к одному обработчику
            check.stateChanged.connect(self.status_KDO)

        # Создаём сетку для размещения элементов
        layout = QGridLayout()

        # Размещаем чекбоксы слева, а управляемые элементы справа
        for row, (check, widget) in enumerate(self.widgets.items()):
            layout.addWidget(check, row, 0)
            layout.addWidget(widget, row, 1)

        self.setLayout(layout)

    # Общий обработчик изменения состояния чекбоксов
    def status_KDO(self, state):
        # Определяем, какой чекбокс отправил сигнал
        check = self.sender()

        # Находим соответствующий ему виджет
        widget = self.widgets[check]

        # Показываем элемент только при установленной галочке
        if check.checkState() == Qt.CheckState.Checked:
            widget.show()
        else:
            widget.hide()

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WidgetsKDO()
    window.show()
    sys.exit(app.exec())