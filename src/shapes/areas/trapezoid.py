from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

from shapes.GUI import InputWindow
from shapes.models.area_models import TrapezoidModel
from shapes.shape import AreaShape


class Trapezoid(AreaShape):
    """
    Вычисляет площадь трапеции.
    """

    def __init__(self):
        super().__init__()
        self.__data = TrapezoidModel()
        self.__input_window = InputWindow("Рассчитать площадь Трапеции")
        self.__gui_name = QLabel("Высота трапеции")
        self.__gui_line = QLineEdit()
        self.__gui_name2 = QLabel("Длина меньшего основания")
        self.__gui_line2 = QLineEdit()
        self.__gui_name3 = QLabel("Длина более длинного основания")
        self.__gui_line3 = QLineEdit()
        self.__gui_button = QPushButton("Рассчитать")
        self.__gui_button.clicked.connect(self.calc_area)
        self.__gui_result = QLabel()

    @property
    def data(self) -> TrapezoidModel:
        return self.__data

    @data.setter
    def data(self, value: TrapezoidModel):
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

    def calc_area(self) -> None:
        try:
            self.data.height = float(self.__gui_line.text())
            self.data.length_min = float(self.__gui_line2.text())
            self.data.length_max = float(self.__gui_line3.text())
            self.data.area = ((self.data.length_min + self.data.length_max) / 2) * self.data.height
            self.__gui_result.setText(str(self.data.area) + " кв.ед.")
        except ValueError as e:
            self.__gui_result.setText("Error")
            print("Неверный ввод, вы должны вводить только цифры!")
