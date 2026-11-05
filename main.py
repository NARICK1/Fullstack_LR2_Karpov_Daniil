import sys
from PyQt6 import uic #импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        #Загружаем ui из qt дизайнера
        uic.loadUi('LR2_Karpov.ui', self)
#проверка, что файл запущен напрямую
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()#создаем объект окна
    window.show()#отрисовываем окна на экране
    sys.exit(app.exec())#обработчик событий