import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    """
    Subclass QMainWindow
    """

    def __init__(self):
        super().__init__()

        # variables
        self.button_is_checked = True

        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        # toggle state of button when clicked
        button.setCheckable(True)
        button.clicked.connect(self.button_toggled)
        button.clicked.connect(self.button_clicked)

        # set fixed size that user is unable to modify
        self.setFixedSize(QSize(400, 300))

        # other options
        # self.setMinimumSize(QSize(400, 300))
        # self.setMaximumSize(QSize(400, 300))

        # set the central widget of the window
        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked...")

    def button_toggled(self, checked):
        self.button_is_checked = checked
        print(f"Checked? {self.button_is_checked}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
