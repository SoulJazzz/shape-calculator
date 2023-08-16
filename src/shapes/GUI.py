import sys
import typing

from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QGridLayout

Application: QApplication = QApplication(sys.argv)


class InputWindow(QWidget):

    def __init__(self, title: str):
        super().__init__()
        self.__grid = QGridLayout()
        self.__grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__grid)
        self.setWindowTitle(title)

    def layout(self) -> typing.Optional['QGridLayout']:
        return super().layout()

    def closeEvent(self, event):
        self.hide()


class Window(QMainWindow):
    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)
        self.__wnd_layout = QVBoxLayout()
        self.__wnd_container = QWidget()
        self.__wnd_container.setLayout(self.__wnd_layout)
        self.setCentralWidget(self.__wnd_container)

    @property
    def wnd_layout(self):
        return self.__wnd_layout

    @property
    def wnd_container(self):
        return self.__wnd_container

    def activate(self):
        # играем музончик
        filename = "intro.mp3"
        player = QMediaPlayer()
        audio_output = QAudioOutput()
        player.setAudioOutput(audio_output)
        player.setSource(QUrl.fromLocalFile(filename))
        audio_output.setVolume(0.25)
        player.play()

        # показываем окошко
        self.show()
        # экзекьютим прогу
        Application.exec()

    def add_button(self, title: str, function) -> None:
        button = QPushButton(title, self)
        button.clicked.connect(function)
        self.wnd_layout.addWidget(button)

    def closeEvent(self, event) -> None:
        exit(0x00)


WINDOW: Window = Window('Shape Calculator v1.0')
