from PIL import Image, ImageFilter
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


    def save(self, prefix):
        
        self.image_path = os.path.join(self.workdir, self.modified_folder, prefix+self.filename)

        sub_path = os.path.join(self.workdir, self.modified_folder)
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)

        self.image.save(self.image_path)

    def makeBW(self):
        self.image = self.image.convert("L")
        self.save("bw_")
        
        
        self.showChoosenImage()

    def turnleft(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.save("left_")
        self.showChoosenImage()

    def turnright(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.save("right_")
        self.showChoosenImage()

    def makeMirror(self):
        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.save("mirror_")
        self.showChoosenImage()

    def makeSharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save("sharp_")
        self.showChoosenImage()
