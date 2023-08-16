from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

from shapes.GUI import InputWindow
from shapes.models.volume_models import ParallelepipedModel
from shapes.shape import VolumeShape


class Parallelepiped(VolumeShape):
    """
    Вычисляет объём прямоугольного параллелепипеда.
    """

    def __init__(self):
        super().__init__()
        self.__data = ParallelepipedModel()
        self.__input_window = InputWindow("Рассчитать площадь Параллелепипеда")
        self.__gui_name = QLabel("Введите ребро параллелепипеда A")
        self.__gui_line = QLineEdit()
        self.__gui_name2 = QLabel("Введите ребро параллелепипеда B")
        self.__gui_line2 = QLineEdit()
        self.__gui_name3 = QLabel("Введите ребро параллелепипеда C")
        self.__gui_line3 = QLineEdit()
        self.__gui_button = QPushButton("Рассчитать")
        self.__gui_button.clicked.connect(self.calc_volume)
        self.__gui_result = QLabel()

    @property
    def data(self) -> ParallelepipedModel:
        return self.__data

    @data.setter
    def data(self, value: ParallelepipedModel):
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
            self.data.edge_a = float(self.__gui_line.text())
            self.data.edge_b = float(self.__gui_line2.text())
            self.data.edge_c = float(self.__gui_line3.text())
            self.data.volume = self.data.edge_a * self.data.edge_b * self.data.edge_c
            self.__gui_result.setText(str(self.data.volume) + " куб.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
