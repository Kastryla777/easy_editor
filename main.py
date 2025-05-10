from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui import Ui_MainWindow

import os

from imageProcessor import ImageProcessor

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow() 

ip = ImageProcessor(ui)

ui.setupUi(win)

workdir = ''
extensions = [".png", ".jpg", ".jpeg", ".gif",]

def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    fileslist = []
    try:
        fileslist = os.listdir(workdir)
    except:
        print("must choose folder")
    fileslist = filter(fileslist, extensions)
    ui.images_list.clear()
    ui.images_list.addItems(fileslist)

def filter(filename: list[str], ext:list[str]):
    image_files = []
    for file in filename:
        for e in ext:
            if file.endswith(e):
                image_files.append(file)

    return image_files



ui.dir_btn.clicked.connect(choose_workdir)



def show_image():
    if ui.images_list.currentItem():
        filename = ui.images_list.currentItem().text()
        ip.open(workdir, filename)
        ip.showChoosenImage()
    else:
        ui.label.setText("Картинка")


ui.images_list.currentItemChanged.connect(show_image)

ui.bw_btn.clicked.connect(ip.makeBW)

win.show()
app.exec()
