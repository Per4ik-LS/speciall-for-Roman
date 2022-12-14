import random
import sys

from random import randint
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
)
from PyQt5.QtGui import (
    QMouseEvent,
    QKeyEvent,
    QPaintEvent,
    QPainter,
    QColor,
    QPolygon,
)

from window_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._init_ui()
        self.should_draw = False

    def _init_ui(self) -> None:
        self.pushButton.clicked.connect(self.print_circle)


    def print_circle(self):
        self.should_draw = True
        self.update()

    def paintEvent(self, event):
        if not self.should_draw:
            return

        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        color = self._get_random_color()
        qp.setBrush(color)
        diametr = random.randint(70, 200)
        start = 60
        qp.drawEllipse(start, start, start + diametr, start + diametr)

    def _get_random_color(self) -> QColor:
        return QColor.fromHsv(randint(0, 359), 255, 255, 255)



app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())