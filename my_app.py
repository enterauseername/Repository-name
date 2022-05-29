from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment = QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
#        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.button.clicked.connect(self.next_click)

app = QApplication([])
main_win = MainWin()
app.exec_()
