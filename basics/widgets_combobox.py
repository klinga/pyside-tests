import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        combo_box = QComboBox()
        combo_box.addItems(["blue", "red", "green"])
        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.InsertAlphabetically)
        combo_box.setMaxCount(10)

        combo_box.currentIndexChanged.connect(
            self.index_changed
        )  # singnal emitted as int
        combo_box.currentTextChanged.connect(self.text_changed)  # signal emitted as str

        self.setCentralWidget(combo_box)

    def index_changed(self, i):
        print(i)

    def text_changed(self, t):
        print(t)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
