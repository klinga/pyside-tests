"""
Same as singals_and_slots_1.py but using PySide2 widgets
"""

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
        self.button = QPushButton("Press me!")
        # toggle state of button when clicked
        self.button.setCheckable(True)

        # released signal is fired but does not send the check state
        self.button.released.connect(self.button_released)

        self.button.setChecked(self.button_is_checked)

        # set the central widget of the window
        self.setCentralWidget(self.button)

    def button_released(self):
        # .isChecked() returns state of the button
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
