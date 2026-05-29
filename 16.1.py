import sys
import requests
from PyQt5 import QtWidgets, QtGui, QtCore


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 650)
        MainWindow.setStyleSheet("background-color: #22222e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 250))
        self.frame.setStyleSheet("background-color: #fb5b5d;")

        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(50, 20, 400, 50))
        self.title_label.setFont(QtGui.QFont("Impact", 18))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setText("Конвертер валют")

        self.input_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cur.setGeometry(QtCore.QRect(50, 280, 400, 50))
        self.input_cur.setFont(QtGui.QFont("Impact", 14))
        self.input_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cur.setPlaceholderText("Из валюты")

        self.input_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sum.setGeometry(QtCore.QRect(50, 350, 400, 50))
        self.input_sum.setFont(QtGui.QFont("Impact", 14))
        self.input_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.input_sum.setPlaceholderText("Сколько")

        self.output_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.output_cur.setGeometry(QtCore.QRect(50, 420, 400, 50))
        self.output_cur.setFont(QtGui.QFont("Impact", 14))
        self.output_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.output_cur.setPlaceholderText("В валюту")

        self.output_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.output_sum.setGeometry(QtCore.QRect(50, 490, 400, 50))
        self.output_sum.setFont(QtGui.QFont("Impact", 14))
        self.output_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sum.setPlaceholderText("Итого")
        self.output_sum.setReadOnly(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 560, 400, 50))
        self.pushButton.setFont(QtGui.QFont("Impact", 14))
        self.pushButton.setText("Конвертация")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 25;
                color: white;
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)

        MainWindow.setWindowTitle("Конвертер валют")


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        try:
            from_cur = self.ui.input_cur.text().upper()
            to_cur = self.ui.output_cur.text().upper()
            amount = float(self.ui.input_sum.text())

            url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
            response = requests.get(url)
            data = response.json()

            result = amount * data["rates"][to_cur]
            self.ui.output_sum.setText(str(round(result, 2)))
        except:
            self.ui.output_sum.setText("Ошибка")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CurrencyConv()
    window.show()
    sys.exit(app.exec_())