from PyQt5.QtGui import QPen, QColor, QGradient, QBrush, QPainter
from PyQt5.QtWidgets import QGraphicsWidget, QGraphicsScene, QGraphicsView, QGraphicsGridLayout, QGraphicsItem

from pyqt_textbox_graphics_widget.textBoxBrowser import TextBoxBrowser


class TextBoxGraphicsWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__scene = QGraphicsScene()
        self.__graphicsView = QGraphicsView()
        browser = TextBoxBrowser()

        browserItem = self.__scene.addWidget(browser)
        lay = QGraphicsGridLayout()
        lay.addItem(browserItem, 0, 0)
        self.setLayout(lay)

        self.setFlag(QGraphicsItem.ItemIsMovable)

    def paint(self, painter, option, widget) -> None:
        pen = QPen(QColor('#777777'), 3)
        gradient = QGradient(QGradient.PremiumDark)
        brush = QBrush(gradient)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRoundedRect(self.rect(), 10.0, 10.0)