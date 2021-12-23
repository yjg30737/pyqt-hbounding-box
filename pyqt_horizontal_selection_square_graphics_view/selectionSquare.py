from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import Qt


class SelectionSquare(QGraphicsRectItem):
    def __init__(self, view, parent=None):
        super().__init__(parent)
        self.__initUi(view)

    def __initUi(self, view=None):
        self.__view = view
        self.setAcceptHoverEvents(True)
        self.setFlags(QGraphicsItem.ItemIsSelectable)
        self.__setStyleOfSelectionSquare()

    def __setStyleOfSelectionSquare(self):
        sq_pen = QPen()
        sq_pen.setStyle(Qt.DashLine)
        sq_pen.setWidth(4)
        self.setPen(sq_pen)

    def mouseMoveEvent(self, e):
        scene_rect = self.__view.scene().sceneRect()
        x = e.pos().x()

        border_rect = self.sceneBoundingRect()

        border_rect_left = border_rect.left()
        border_rect_right = border_rect.right()

        scene_rect_right = scene_rect.right()-5

        if abs(x-border_rect_left) > abs(x-border_rect_right):
            if e.buttons() & Qt.LeftButton:
                right = scene_rect_right if x > scene_rect_right else x
                rect = self.rect()
                rect.setRight(right)
                self.setRect(rect)
        else:
            if e.buttons() & Qt.LeftButton:
                if x < 0:
                    x = 0
                left = x
                rect = self.rect()
                rect.setLeft(left)
                self.setRect(rect)
        return super().mouseMoveEvent(e)

    def hoverEnterEvent(self, e):
        return super().hoverEnterEvent(e)

    def hoverMoveEvent(self, e):
        x = int(e.pos().x())
        selection_rect = self.sceneBoundingRect()
        if x in range(int(selection_rect.left()), int(selection_rect.left())+5):
            self.setCursor(Qt.SizeHorCursor)
        elif x in range(int(selection_rect.right())-10, int(selection_rect.right())):
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.unsetCursor()
        return super().hoverMoveEvent(e)

    def hoverLeaveEvent(self, e):
        return super().hoverLeaveEvent(e)