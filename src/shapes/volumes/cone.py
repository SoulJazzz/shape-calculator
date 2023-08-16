import math

from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

from shapes.GUI import InputWindow
from shapes.models.volume_models import ConeModel
from shapes.shape import VolumeShape


class Cone(VolumeShape):
    """
    Вычисляет объём конуса.
    """

    def __init__(self):
        super().__init__()
        self.__data = ConeModel()
        self.__input_window = InputWindow("Рассчитать площадь Конуса")
        self.__gui_name = QLabel("Введите радиус основания")
        self.__gui_line = QLineEdit()
        self.__gui_result = QLabel()
        self.__gui_name2 = QLabel("Введите высоту")
        self.__gui_line2 = QLineEdit()
        self.__gui_result2 = QLabel()
        self.__gui_button = QPushButton("Рассчитать")
        self.__gui_button.clicked.connect(self.calc_volume)
        self.__gui_result = QLabel()

    @property
    def data(self) -> ConeModel:
        return self.__data

    @data.setter
    def data(self, value: ConeModel):
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_name2, 2, 0)
            self.__input_window.layout().addWidget(self.__gui_line2, 2, 1)
            self.__input_window.layout().addWidget(self.__gui_button, 3, 0)
            self.__input_window.layout().addWidget(self.__gui_result, 3, 1)
            self.__input_window.show()

    def calc_volume(self) -> None:
        try:
            self.data.base_radius = float(self.__gui_line.text())
            self.data.height = float(self.__gui_line2.text())
            self.data.volume = 1 / 3 * math.pi * self.data.base_radius ** 2 * self.data.height
            self.__gui_result.setText(str(self.data.volume) + " куб.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
