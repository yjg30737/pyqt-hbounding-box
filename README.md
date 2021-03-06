# pyqt-hbounding-box
PyQt QGraphicsView with bounding box. User can move vertical border of the box horizontally.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-hbounding-box`

## Feature
* Being able to drag and drop vertical border horizontally
* Pressing mouse cursor to place more adjacent border on the spot.
* Right click to release the focus of the box
* You can set the background out of the box darker with `setDarkerOutOfBox(f: bool)`.

## Example
Code Sample

```python
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QFileDialog

from pyqt_hbounding_box.hboundingBox import HBoundingBox


class HBoundingBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        addImageBtn = QPushButton('Add image')
        addImageBtn.clicked.connect(self.__addImage)
        self.__view = HBoundingBox()

        lay = QGridLayout()
        lay.addWidget(addImageBtn)
        lay.addWidget(self.__view)

        self.setLayout(lay)

    def __addImage(self):
        filename = QFileDialog.getOpenFileName(self, 'Open', '', 'Image Files (*.png *.jpg *.bmp)')
        if filename[0]:
            filename = filename[0]
            self.__view.setFile(filename)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = HBoundingBoxExample()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/147186296-fa9083d0-67c6-4d7e-b139-7845ee38ddf9.mp4

## See Also
* <a href="https://github.com/yjg30737/pyqt-vbounding-box.git">pyqt-vbounding-box</a> - vertical way
* <a href="https://github.com/yjg30737/pyqt-bounding-box.git">pyqt-bounding-box</a> - horizontal/vertical ways


