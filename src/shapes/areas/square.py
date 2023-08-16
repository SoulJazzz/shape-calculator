from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

from shapes.GUI import InputWindow
from shapes.models.area_models import SquareModel
from shapes.shape import AreaShape


class Square(AreaShape):
    """
    Вычисляет площадь квадрата.
    """

    def __init__(self):
        super().__init__()
        self.__data = SquareModel()
        self.__input_window = InputWindow("Рассчитать площадь Квадрата")
        self.__gui_text = QLabel("Результат")
        self.__gui_name = QLabel("Размер стороны")
        self.__gui_button = QPushButton("=")
        self.__gui_button.setFixedWidth(24)
        self.__gui_button.clicked.connect(self.calc_area)
        self.__gui_line = QLineEdit()
        self.__gui_result = QLabel()

    @property
    def data(self) -> SquareModel:
        return self.__data

    @data.setter
    def data(self, value: SquareModel):
        self.__data = value

    def input_data(self) -> None:
        if self.__input_window.isHidden():
            self.__input_window.layout().addWidget(self.__gui_text, 0, 3)
            self.__input_window.layout().addWidget(self.__gui_name, 1, 0)
            self.__input_window.layout().addWidget(self.__gui_line, 1, 1)
            self.__input_window.layout().addWidget(self.__gui_button, 1, 2)
            self.__input_window.layout().addWidget(self.__gui_result, 1, 3)
            self.__input_window.show()

    def calc_area(self) -> None:
        try:
            self.data.side = float(self.__gui_line.text())
            self.data.area = pow(self.data.side, 2)
            self.__gui_result.setText(str(self.data.area) + " кв.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
