import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Пользовательские исключения
class EmptyFieldError(Exception):
    pass

class InvalidNameError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass

# XML-разметка интерфейса из Qt Designer
tempKDO = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="Name">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>70</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="LastName">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>130</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="LastNameLabel">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>110</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Фамилия</string>
    </property>
   </widget>
   <widget class="QLabel" name="nameLabel">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>50</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QPushButton" name="addStudentBtn">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>170</y>
      <width>141</width>
      <height>81</height>
     </rect>
    </property>
    <property name="sizePolicy">
     <sizepolicy hsizetype="Minimum" vsizetype="Preferred">
      <horstretch>0</horstretch>
      <verstretch>0</verstretch>
     </sizepolicy>
    </property>
    <property name="text">
     <string>Добавить в список</string>
    </property>
   </widget>
   <widget class="QListWidget" name="presenceList">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>60</y>
      <width>256</width>
      <height>241</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="listLabel">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>30</y>
      <width>161</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Список присутствующих</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

# Класс приложения «Список присутствующих»
class GroupList_KDO(QMainWindow):

    def __init__(self):
        super().__init__()

        # Загружаем интерфейс из строки
        f = io.StringIO(tempKDO)
        uic.loadUi(f, self)

        # Подгоняем размер кнопки
        self.addStudentBtn.adjustSize()

        # Подключаем кнопку к обработчику
        self.addStudentBtn.clicked.connect(self.status_KDO)

    # Проверка имени или фамилии
    def check_name_KDO(self, value, field_name):

        # Проверяем пустое поле
        if not value:
            raise EmptyFieldError(
                f"Поле «{field_name}» не должно быть пустым."
            )

        # Проверяем минимальную длину
        if len(value) < 3:
            raise InvalidNameError(
                f"Поле «{field_name}» должно содержать "
                "не менее 3 букв."
            )

        # Проверяем, что введены только буквы
        if not value.isalpha():
            raise InvalidNameError(
                f"Поле «{field_name}» должно содержать "
                "только буквы, без цифр и пробелов."
            )

        # Делаем первую букву заглавной
        return value.capitalize()

    # Обработчик добавления студента
    def status_KDO(self):

        try:
            # Получаем данные из полей
            name = self.Name.text().strip()
            lastname = self.LastName.text().strip()

            # Проверяем имя и фамилию
            name = self.check_name_KDO(name, "Имя")
            lastname = self.check_name_KDO(lastname, "Фамилия")

            # Формируем запись
            student = lastname + " " + name

            # Проверяем наличие дубликата
            for i in range(self.presenceList.count()):
                if self.presenceList.item(i).text().lower() == student.lower():
                    raise DuplicateStudentError(
                        "Этот студент уже есть в списке."
                    )

            # Добавляем студента
            self.presenceList.addItem(student)

            # Очищаем поля
            self.Name.clear()
            self.LastName.clear()

            # Возвращаем курсор в поле имени
            self.Name.setFocus()

        except (EmptyFieldError, InvalidNameError,
                DuplicateStudentError) as error:

            # Показываем сообщение об ошибке
            QMessageBox.warning(
                self,
                "Ошибка ввода",
                str(error)
            )

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroupList_KDO()
    window.show()
    sys.exit(app.exec())