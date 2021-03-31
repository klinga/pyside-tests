import sys

from PySide2.QtWidgets import QApplication, QWidget

# only one QApplication instance is needed per application
app = QApplication(sys.argv)
window = QWidget()
# windows without a parent are hidden by default
window.show()
# start event loop
app.exec_()
