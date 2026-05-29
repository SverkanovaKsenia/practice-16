import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Ui_TempConverter:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 350)
        MainWindow.setStyleSheet("background-color: #22222e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 120))
        self.frame.setStyleSheet("background-color: #fb5b5d;")

        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(50, 20, 300, 50))
        self.title_label.setFont(QtGui.QFont("Impact", 16))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setText("Конвертер температур")

        self.input_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.input_temp.setGeometry(QtCore.QRect(50, 150, 300, 40))
        self.input_temp.setFont(QtGui.QFont("Impact", 14))
        self.input_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.input_temp.setPlaceholderText("Введите температуру")

        self.btn_to_celsius = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_celsius.setGeometry(QtCore.QRect(50, 210, 140, 40))
        self.btn_to_celsius.setText("→ °C")
        self.btn_to_celsius.setFont(QtGui.QFont("Impact", 12))
        self.btn_to_celsius.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 10;
                color: white;
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)

        self.btn_to_fahrenheit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_fahrenheit.setGeometry(QtCore.QRect(210, 210, 140, 40))
        self.btn_to_fahrenheit.setText("→ °F")
        self.btn_to_fahrenheit.setFont(QtGui.QFont("Impact", 12))
        self.btn_to_fahrenheit.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 10;
                color: white;
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)

        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(50, 270, 300, 40))
        self.output_label.setFont(QtGui.QFont("Impact", 14))
        self.output_label.setStyleSheet("color: white; background-color: #333; border-radius: 5;")
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setText("Результат")

        MainWindow.setWindowTitle("Конвертер температур")


class TempConverter(QtWidgets.QMainWindow):
    def __init__(self):
        super(TempConverter, self).__init__()
        self.ui = Ui_TempConverter()
        self.ui.setupUi(self)
        self.ui.btn_to_celsius.clicked.connect(self.to_celsius)
        self.ui.btn_to_fahrenheit.clicked.connect(self.to_fahrenheit)

    def to_celsius(self):
        try:
            f = float(self.ui.input_temp.text())
            c = (f - 32) * 5 / 9
            self.ui.output_label.setText(f"{f}°F = {round(c, 1)}°C")
        except:
            self.ui.output_label.setText("Ошибка ввода")

    def to_fahrenheit(self):
        try:
            c = float(self.ui.input_temp.text())
            f = c * 9 / 5 + 32
            self.ui.output_label.setText(f"{c}°C = {round(f, 1)}°F")
        except:
            self.ui.output_label.setText("Ошибка ввода")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TempConverter()
    window.show()
    sys.exit(app.exec_())