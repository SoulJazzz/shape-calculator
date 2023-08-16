"""
Абстрактный класс фигуры
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def input_data(self) -> None:
        pass


class AreaShape(Shape):
    @abstractmethod
    def calc_area(self) -> None:
        pass


class VolumeShape(Shape):
    @abstractmethod
    def calc_volume(self) -> None:
        pass
