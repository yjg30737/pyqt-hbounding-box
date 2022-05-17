from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap, QColor, QBrush, QPalette, QPen, QPainterPath
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem

from pyqt_hbounding_box.item import Item


class HBoundingBox(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__p = 0
        self.__scene = 0
        self.__graphicItem = 0
        self.__sq = 0
        self.__pathItem = 0
        self.__pressed = False

    def mousePressEvent(self, e):
        if self.__sq and e.button() == Qt.LeftButton:
            if isinstance(self.__sq, Item):
                scene_rect = self.__sq.sceneBoundingRect()
                scene_pos = self.mapToScene(e.pos())
                if scene_rect.contains(scene_pos):
                    rect = self.__sq.rect()
                    scene_pos_x = scene_pos.x()
                    if abs(rect.right()-scene_pos_x) > abs(rect.left()-scene_pos_x):
                        rect.setLeft(scene_pos_x)
                        self.__sq.setRect(rect)
                    else:
                        rect.setRight(scene_pos_x)
                        self.__sq.setRect(rect)
                else:
                    rect = self.__sq.rect()
                    scene_pos_x = scene_pos.x()
                    if scene_pos_x < 0:
                        scene_pos_x = 0
                        rect.setLeft(scene_pos_x)
                        self.__sq.setRect(rect)
                    elif rect.left() > scene_pos_x:
                        rect.setLeft(scene_pos_x)
                        self.__sq.setRect(rect)
                    elif scene_pos_x > self.__scene.sceneRect().right():
                        scene_pos_x = self.__scene.sceneRect().right()-self.__sq.pen().width()//2
                        rect.setRight(scene_pos_x)
                        self.__sq.setRect(rect)
                    else:
                        rect.setRight(scene_pos_x)
                        self.__sq.setRect(rect)
        return super().mousePressEvent(e)

    def setFile(self, filename):
        self.__p = QPixmap(filename)
        self.__setPixmap(self.__p)

    def __setPixmap(self, p):
        self.__p = p
        self.__scene = QGraphicsScene()
        self.__scene.installEventFilter(self)

        self.__graphicItem = self.__scene.addPixmap(self.__p)
        self.setScene(self.__scene)
        # fit in view literally
        self.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        self.show()

        self.__sq = Item(view=self)
        self.__sq.setRect(self.sceneRect())
        self.scene().addItem(self.__sq)

    def resizeEvent(self, e):
        if isinstance(self.__graphicItem, QGraphicsItem):
            self.fitInView(self.__graphicItem, Qt.KeepAspectRatio)
        return super().resizeEvent(e)

    def __setDarkerOutOfBox(self):
        br = self.__sq.sceneBoundingRect()
        l = br.left()
        r = br.right()
        exRect = self.__graphicItem.boundingRect()
        inRect = QRectF(self.__sq.sceneBoundingRect())

        self.__path = QPainterPath()
        self.__path.addRect(exRect)
        self.__path.moveTo(inRect.topLeft())
        self.__path.addRect(inRect)

        b = QBrush(QColor(10, 10, 10, 100))
        p = QPen(Qt.NoPen)
        if self.__pathItem:
            self.scene().removeItem(self.__pathItem)
        self.__pathItem = self.scene().addPath(self.__path, p, b)

    def eventFilter(self, obj, e):
        if e.type() == 156:
            self.__pressed = True
            self.__setDarkerOutOfBox()
        elif e.type() == 155:
            if self.__pressed:
                self.__setDarkerOutOfBox()
        elif e.type() == 157:
            self.__pressed = False
        return super().eventFilter(obj, e)