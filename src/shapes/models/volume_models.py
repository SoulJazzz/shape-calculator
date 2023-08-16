"""
Описание схем объектов фигур 3D (DTO).
"""

from pydantic import BaseModel


class SphereModel(BaseModel):
    """
    Модель сферы:

    .. code-block::

        SphereModel(
            radius=83,
            volume=2395406.339(м³)
    """

    radius: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float


class CubeModel(BaseModel):
    """
    Модель куба:

    .. code-block::

        CubeModel(
            edge=63.7,
            volume=258474.853(м³)
    """
    edge: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float


class PyramidModel(BaseModel):
    """
    Модель пирамиды:

    .. code-block::

        PyramidModel(
            base_side=65,
            number_of_sides=4,
            pyramid_height=50,
            result=112756.422(м³)
    """

    base_side: float = 0
    number_of_sides: float = 0
    pyramid_height: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float


class ParallelepipedModel(BaseModel):
    """
    Модель прямоугольного параллелепипеда:

    .. code-block::

        ParallelepipedModel(
            edge_a=25,
            edge_b=30,
            edge_c=18,
            volume=13500(м³)
    """
    edge_a: float = 0
    edge_b: float = 0
    edge_c: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float


class CylinderModel(BaseModel):
    """
    Модель цилиндра:

    .. code-block::

        CylinderModel(
            cylinder_radius=25,
            cylinder_height=30,
            volume=58912.5(м³)
    """

    cylinder_radius: float = 0
    cylinder_height: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float


class ConeModel(BaseModel):
    """
    Модель конуса:

    .. code-block::

        ConeModel(
            base_radius=50,
            height=80,
            volume=209466.667(м³)
    """

    base_radius: float = 0
    height: float = 0
    volume: float = 0

    class Config:
        arbitrary_types_allowed = True
        ignored_types = float
