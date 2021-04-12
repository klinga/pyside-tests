import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow
from PySide2.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        labelA = QLabel("Hello")
        font = labelA.font()
        font.setPointSize(30)
        labelA.setFont(font)
        labelA.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(labelA)

        labelB = QLabel()
        labelB.setPixmap(QPixmap("../resources/check-icon.png"))
        labelB.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(labelB)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
