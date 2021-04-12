import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        listw = QListWidget()
        listw.addItems(["one", "two", "three", "four", "five"])

        listw.currentItemChanged.connect(self.index_changed)
        listw.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(listw)

    def index_changed(self, current, previous):
        try:
            print((previous.text(), current.text()))
        except AttributeError:
            # needed for initial run, when previous does not exist, and top one is selected by
            # default
            pass

    def text_changed(self, t):
        print(t)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
