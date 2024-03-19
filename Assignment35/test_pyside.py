import cv2
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.my_btn = QPushButton()
        self.my_btn.setText("hello world")
        layout.addWidget(self.my_btn)

        

        self.my_lb = QLabel()
        layout.addWidget(self.my_lb)
        
        img = cv2.imread("input/wp.jpg")
         
        img = cv2.resize(img,(400,500))
        img_qt = QImage(img,img.shape[1],img.shape[0],QImage.Format.Format_RGB888)
        self.my_lb.setPixmap(QPixmap.fromImage(img_qt))
    

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()