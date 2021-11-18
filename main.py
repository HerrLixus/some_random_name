import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()

    def initUi(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)
        self.draw_function(painter)

        painter.end()

    def draw_function(self, painter):
        brush = QBrush(QColor(255, 255, 0))
        painter.setBrush(brush)
        for i in range(random.randint(1, 10)):
            x, y = random.randint(0, 350), random.randint(0, 350)
            size = random.randint(0, 350)

            painter.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
