"""
Same as singals_and_slots_1.py but using PySide2 widgets
"""

import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    """
    Subclass QMainWindow
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press me!")
        # toggle state of button when clicked
        self.button.setCheckable(True)

        # released signal is fired but does not send the check state
        self.button.clicked.connect(self.button_clicked)

        # set the central widget of the window
        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("You already clicked me...")

        # disable the button
        self.button.setEnabled(False)

        self.setWindowTitle("One Shot App.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
