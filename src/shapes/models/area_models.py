"""
Описание схем объектов фигур 2D (DTO).
"""
from pydantic import BaseModel


class RectangleModel(BaseModel):
    """
    Модель прямоугольника:

    .. code-block::

        RectangleModel(
            length=70,
            width=40,
            square=2800(м²)
    """

    length: float = 0
    width: float = 0
    area: float = 0


class CircleModel(BaseModel):
    """
    Модель круга:

    .. code-block::

        CircleModel(
            radius=70,
            square=7855(м²)
    """

    radius: float = 0
    area: float = 0


class SquareModel(BaseModel):
    """
    Модель квадрата:

    .. code-block::

        SquareModel(
            side=30,
            square=900(м²)
    """

    side: float = 0
    area: float = 0


class TriangleModel(BaseModel):
    """
    Модель треугольника:

    .. code-block::

        TriangleModel(
            side_a=20,
            side_b=25,
            side_c=30,
            S=248.039(м²),
            Ma=25.73907535(м²),
            Mb=22.22048604(м²),
            Mc=16.95582496(м²)
    """

    a: float = 0
    b: float = 0
    c: float = 0
    area: float = 0
    mA: float = 0
    mB: float = 0
    mC: float = 0

    def medians_to_str(self):
        return f"A = {self.mA}, B={self.mB}, C={self.mC}"


class TrapezoidModel(BaseModel):
    """
    Модель трапеции:

    .. code-block::

        TrapezoidModel(
            height=40,
            length_min=40,
            length_max=60,
            square=2000(м²)
    """

    height: float = 0
    length_min: float = 0
    length_max: float = 0
    area: float = 0


class RhombusModel(BaseModel):
    """
    Модель ромба:

    .. code-block::

        RhombusModel(
            diagonals_1=35.5,
            diagonals_2=42,
            square=745.5(м²),
    """
    diagonals_1: float = 0
    diagonals_2: float = 0
    area: float = 0
