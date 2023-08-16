import math

from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel

from shapes.GUI import InputWindow
from shapes.models.area_models import TriangleModel
from shapes.shape import AreaShape


class Triangle(AreaShape):
    """
    Вычисляет площадь треугольника.
    """

    def __init__(self):
        super().__init__()
        self.__data = TriangleModel()
        self.__input_window = InputWindow("Рассчитать площадь/медиану Треугольника")
        self.__gui_name = QLabel("Введите сторону A")
        self.__gui_line = QLineEdit()
        self.__gui_name2 = QLabel("Введите сторону B")
        self.__gui_line2 = QLineEdit()
        self.__gui_name3 = QLabel("Введите сторону C")
        self.__gui_line3 = QLineEdit()
        self.__gui_result_button = QPushButton("Рассчитать площадь")
        self.__gui_result_button.clicked.connect(self.calc_area)
        self.__gui_result_text = QLabel()
        self.__gui_result_button2 = QPushButton("Рассчитать медиану")
        self.__gui_result_button2.clicked.connect(self.calc_median)
        self.__gui_result_text2 = QLabel()

    @property
    def data(self) -> TriangleModel:
        return self.__data

    @data.setter
    def data(self, value: TriangleModel) -> None:
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_name2, 2, 0)
            self.__input_window.layout().addWidget(self.__gui_line2, 2, 1)
            self.__input_window.layout().addWidget(self.__gui_name3, 3, 0)
            self.__input_window.layout().addWidget(self.__gui_line3, 3, 1)
            self.__input_window.layout().addWidget(self.__gui_result_button, 4, 0)
            self.__input_window.layout().addWidget(self.__gui_result_text, 5, 0)
            self.__input_window.layout().addWidget(self.__gui_result_button2, 4, 1)
            self.__input_window.layout().addWidget(self.__gui_result_text2, 5, 1)
            self.__input_window.show()

    def calc_area(self) -> None:
        try:
            self.data.a = float(self.__gui_line.text())
            self.data.b = float(self.__gui_line2.text())
            self.data.c = float(self.__gui_line3.text())

            half_perimeter = (self.data.a + self.data.b + self.data.c) / 2
            self.data.area = (half_perimeter
                              * (half_perimeter - self.data.a)
                              * (half_perimeter - self.data.b)
                              * (half_perimeter - self.data.c))

            if self.data.area <= 0:
                raise KeyError()

            self.data.area = math.sqrt(self.data.area)
            self.__gui_result_text.setText(str(self.data.area) + " кв.ед.")
        except ValueError as e:
            self.__gui_result_text.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
        except KeyError as e:
            self.__gui_result_text.setText("Error")
            print("Одна сторона равна (или больше) сумме двух других сторон.")

    def calc_median(self) -> None:
        try:
            self.data.a = float(self.__gui_line.text())
            self.data.b = float(self.__gui_line2.text())
            self.data.c = float(self.__gui_line3.text())

            sum_c = 2 * (self.data.c ** 2)
            sum_b = 2 * (self.data.b ** 2)
            sum_a = 2 * (self.data.a ** 2)

            pow_a = self.data.a ** 2
            pow_b = self.data.b ** 2
            pow_c = self.data.c ** 2

            pre_sqrt_1 = sum_c + sum_b - pow_a
            if pre_sqrt_1 < 0:
                raise KeyError()

            pre_sqrt_2 = sum_c + sum_a - pow_b
            if pre_sqrt_2 < 0:
                raise KeyError()

            pre_sqrt_3 = sum_a + sum_b - pow_c
            if pre_sqrt_3 < 0:
                raise KeyError()

            self.data.mA = math.sqrt(pre_sqrt_1)
            self.data.mB = math.sqrt(pre_sqrt_2)
            self.data.mC = math.sqrt(pre_sqrt_3)

            self.__gui_result_text2.setText(self.data.medians_to_str())
        except ValueError as e:
            self.__gui_result_text2.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
