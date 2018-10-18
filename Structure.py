from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from face_datasets import create_dataset
from training import train_data
from face_recognition import recognize
import sys

class First(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowIcon(QIcon('eye.png'))

        self.photo = QLabel(self)
        pixmap = QPixmap('robo_logo.png')
        pixmap = pixmap.scaledToHeight(40)
        self.photo.setPixmap(pixmap)
        self.photo.resize(40, 40)
        self.photo.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self)
        self.label.setText('Enter Name:')
        self.textbox = QLineEdit(self)
        self.textbox.setText('')
        self.textbox.resize(120, 20)


        self.btn = QPushButton('Add Person to DataSet', self)
        self.btn.setToolTip('Starts adding photos to dataset')
        self.btn.setFlat(False)
       # btn.resize(btn.sizeHint())
        #btn.move(0, 150)
        self.btn.clicked.connect(self.add_new)



        self.recognize_button = QPushButton('', self)
        self.recognize_button.setToolTip('Shows your true self')
        self.recognize_button.clicked.connect(self.recognizer)
        self.recognize_button.setIcon(QIcon('eye.png'))
        self.recognize_button.setFlat(False)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label)
        hbox1.addWidget(self.textbox)
        fbox = QFormLayout()
        fbox.addRow(hbox1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(self.recognize_button)
        vbox.addWidget(self.photo)
        fbox.addRow(vbox)
        self.setLayout(fbox)

        self.setFixedSize(250, 150)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Recognizer')
        self.show()


    def add_new(self):
        name = self.textbox.text()
        self.textbox.setText("")
        self.recognize_button.setIcon(QIcon('eye_green.png'))
        f = open("FaceId.txt", "r")
        id = f.readline()
        f.close()
        f = open("line_for_if.txt", "a")
        f.write("\n" + name + "\t" + str(id))
        f.close()

        create_dataset()
        train_data()
        self.recognize_button.setIcon(QIcon('eye.png'))
    def recognizer(self):
        self.recognize_button.setIcon(QIcon('eye_green.png'))
        recognize()
        self.recognize_button.setIcon(QIcon('eye.png'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = First()
    sys.exit(app.exec_())
