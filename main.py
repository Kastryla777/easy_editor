from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow() 

ui.setupUi(win)



win.show()
app.exec()