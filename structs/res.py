from PySide6.QtCore import QUrl


class AppRes:
    path_image = 'images'

    def getImagePath(self) -> str:
        return self.path_image
