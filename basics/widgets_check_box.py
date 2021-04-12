import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        check_box = QCheckBox("Test checkbox")
        check_box.setCheckState(Qt.Checked)
        check_box.stateChanged.connect(self.show_state)

        self.setCentralWidget(check_box)

    def show_state(self, s):
        # Qt.Checked
        # Qt.Unchecked
        # Qt.PartiallyChecked

        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
