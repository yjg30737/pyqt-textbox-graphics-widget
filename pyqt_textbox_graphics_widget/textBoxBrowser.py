from PyQt5.QtGui import QTextOption, QFont
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtCore import Qt


class TextBoxBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.setReadOnly(False)
        self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.setStyleSheet('QTextBrowser { background-color: transparent; color: #DDD; border: 0; }')
        self.setFont(QFont('Arial', 18))
        # todo change fixedheight as minimum if it is necessary
        self.setFixedHeight(self.fontMetrics().boundingRect('M').height()+2)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cursorPositionChanged.connect(self.__setNewFixedHeightForLines)
        self.setWordWrapMode(QTextOption.NoWrap)

    def __setNewFixedHeightForLines(self):
        self.setFixedWidth(max(self.sizeHint().width(), self.document().idealWidth()))
        self.setFixedHeight((self.fontMetrics().boundingRect('M').height()+2)*self.document().lineCount()+2)