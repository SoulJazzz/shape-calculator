import math

from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

from shapes.GUI import InputWindow
from shapes.models.volume_models import PyramidModel
from shapes.shape import VolumeShape


class Pyramid(VolumeShape):
    """
    Вычисляет объём пирамиды.
    """

    def __init__(self):
        super().__init__()
        self.__data = PyramidModel()
        self.__input_window = InputWindow("Рассчитать площадь Пирамиды")
        self.__gui_name = QLabel("Введите сторону основания")
        self.__gui_line = QLineEdit()
        self.__gui_name2 = QLabel("Введите количество сторон")
        self.__gui_line2 = QLineEdit()
        self.__gui_name3 = QLabel("Введите высоту пирамиды")
        self.__gui_line3 = QLineEdit()
        self.__gui_button = QPushButton("Рассчитать")
        self.__gui_button.clicked.connect(self.calc_volume)
        self.__gui_result = QLabel()

    @property
    def data(self) -> PyramidModel:
        return self.__data

    @data.setter
    def data(self, value: PyramidModel):
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_name2, 2, 0)
            self.__input_window.layout().addWidget(self.__gui_line2, 2, 1)
            self.__input_window.layout().addWidget(self.__gui_name3, 3, 0)
            self.__input_window.layout().addWidget(self.__gui_line3, 3, 1)
            self.__input_window.layout().addWidget(self.__gui_button, 4, 0)
            self.__input_window.layout().addWidget(self.__gui_result, 4, 1)
            self.__input_window.show()

    def calc_volume(self) -> None:
        try:
            self.data.base_side = float(self.__gui_line.text())
            self.data.number_of_sides = float(self.__gui_line2.text())
            self.data.pyramid_height = float(self.__gui_line3.text())
            numerator = self.data.base_side ** 2 * self.data.number_of_sides * self.data.pyramid_height
            denominator = 12.0 * math.tan(math.radians(180 / self.data.number_of_sides))
            self.data.volume = numerator / denominator
            self.__gui_result.setText(str(self.data.volume) + " куб.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
