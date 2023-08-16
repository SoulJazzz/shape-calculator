from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit

from shapes.GUI import InputWindow
from shapes.models.volume_models import CubeModel
from shapes.shape import VolumeShape


class Cube(VolumeShape):
    """
    Вычисляет объёма куба.
    """

    def __init__(self):
        super().__init__()
        self.__data = CubeModel()
        self.__input_window = InputWindow("Рассчитать площадь Куба")
        self.__gui_text = QLabel("Результат")
        self.__gui_name = QLabel("Введите размер ребра куба")
        self.__gui_button = QPushButton("=")
        self.__gui_button.setFixedWidth(24)
        self.__gui_button.clicked.connect(self.calc_volume)
        self.__gui_line = QLineEdit()
        self.__gui_result = QLabel()

    @property
    def data(self) -> CubeModel:
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_text, 0, 3)
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_button, 1, 2)
            self.__input_window.layout().addWidget(self.__gui_result, 1, 3)
            self.__input_window.show()

    def calc_volume(self) -> None:
        try:
            self.data.edge = float(self.__gui_line.text())
            self.data.volume = self.data.edge ** 3
            self.__gui_result.setText(str(self.data.volume) + " куб.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
