# pyqt-textbox-graphics-widget
PyQt text box which is movable, auto-resizable by text size. Parent class is QGraphicsWidget.

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-textbox-graphics-widget.git --upgrade```

## Usage
You can move the box if you drag any areas near the border. If you click any areas near the middle of the box, cursor will be shown to let you write something down. Box will be auto-resized by text size. (See the result below)

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow
from pyqt_textbox_graphics_widget import TextBoxGraphicsWidget


class DiagramMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        view = QGraphicsView()

        self.__scene = QGraphicsScene()
        self.__scene.setSceneRect(0, 0, 400, 400)
        
        textBox = TextBoxGraphicsWidget()
        self.__scene.addItem(textBox)
        view.setScene(self.__scene)

        self.setCentralWidget(view)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    diagramMainWindow = DiagramMainWindow()
    diagramMainWindow.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/153204254-cd5776c3-54c3-47a5-9285-98229b0376b1.mp4

## See Also
* <a href="https://github.com/yjg30737/pyqt-styled-graphics-text-item-example.git">pyqt-styled-graphics-text-item-example</a> - This is based on ```QGraphicsTextItem```. In terms of usefulness, ```pyqt-styled-graphics-text-item-example``` is more inferior than this one.  


