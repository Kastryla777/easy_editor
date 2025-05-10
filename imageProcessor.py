from PIL import Image 
from ui import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os 




class ImageProcessor():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.image = None
        self.filename = None
        self.modified_folder = "modified"

    def open(self, workdir, filename):
        self.filename = filename
        self.workdir = workdir
        self.image_path = os.path.join(workdir, filename)

        self.image = Image.open(self.image_path)



    def showChoosenImage(self):
        if self.image:
            self.ui.label.hide()

            pixmap = QPixmap(self.image_path)
            w, h = self.ui.label.width(), self.ui.label.height()
            pixmap = pixmap.scaled(w,h, Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.label.setPixmap(pixmap)


            self.ui.label.show()


    def makeBW(self):
        bw = self.image.convert("L")

        
        self.image_path = os.path.join(self.workdir, self.modified_folder, "bw_"+self.filename)

        sub_path = os.path.join(self.workdir, self.modified_folder)
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)

        bw.save(self.image_path)

        self.showChoosenImage()