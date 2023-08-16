from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

from shapes.GUI import InputWindow
from shapes.models.area_models import RhombusModel
from shapes.shape import AreaShape


class Rhombus(AreaShape):
    """
    Вычисляет площадь ромба.
    """

    def __init__(self):
        super().__init__()
        self.__data = RhombusModel()
        self.__input_window = InputWindow("Рассчитать площадь Ромба")
        self.__gui_name = QLabel("Введите диагональ ромба d1")
        self.__gui_line = QLineEdit()
        self.__gui_result = QLabel()
        self.__gui_name2 = QLabel("Введите диагональ ромба d2")
        self.__gui_line2 = QLineEdit()
        self.__gui_result2 = QLabel()
        self.__gui_result_button = QPushButton("Рассчитать")
        self.__gui_result_button.clicked.connect(self.calc_area)
        self.__gui_result_text = QLabel()
        self.__gui_result_text.setFont(QFont('Times', 10))

    @property
    def data(self) -> RhombusModel:
        return self.__data

    @data.setter
    def data(self, value: RhombusModel):
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_name2, 2, 0)
            self.__input_window.layout().addWidget(self.__gui_line2, 2, 1)
            self.__input_window.layout().addWidget(self.__gui_result_button, 3, 0)
            self.__input_window.layout().addWidget(self.__gui_result_text, 3, 1)
            self.__input_window.show()

    def calc_area(self) -> None:
        try:
            self.data.diagonals_1 = float(self.__gui_line.text())
            self.data.diagonals_2 = float(self.__gui_line2.text())
            self.data.area = (self.data.diagonals_1 * self.data.diagonals_2) / 2
            self.__gui_result_text.setText(str(self.data.area) + " кв.ед.")
        except ValueError as e:
            self.__gui_result_text.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
