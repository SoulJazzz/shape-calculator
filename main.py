from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from shapes.GUI import WINDOW
from shapes.areas.circle import Circle
from shapes.areas.rectangle import Rectangle
from shapes.areas.rhombus import Rhombus
from shapes.areas.square import Square
from shapes.areas.trapezoid import Trapezoid
from shapes.areas.triangle import Triangle
from shapes.volumes.cone import Cone
from shapes.volumes.cube import Cube
from shapes.volumes.cylinder import Cylinder
from shapes.volumes.parallelepiped import Parallelepiped
from shapes.volumes.pyramid import Pyramid
from shapes.volumes.sphere import Sphere

shapes = {
    1: {
        1: Rectangle(),
        2: Circle(),
        3: Square(),
        4: Triangle(),
        5: Trapezoid(),
        6: Rhombus()
    },
    2: {
        1: Sphere(),
        2: Cube(),
        3: Pyramid(),
        4: Parallelepiped(),
        5: Cylinder(),
        6: Cone()
    }
}

if __name__ == "__main__":
    # Центруем весь контент в окне
    WINDOW.wnd_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    # Рисуем GUI со всеми возможными калькуляторами по геометрическим фигурам
    key: int = 1
    for dct in shapes.values():
        if key == 2:
            WINDOW.wnd_layout.addWidget(QLabel("-------3D Shapes-------"))
        else:
            WINDOW.wnd_layout.addWidget(QLabel("-------2D Shapes-------"))

        for index in dct.values():
            WINDOW.add_button(index.__class__.__name__, index.input_data)
        key += 1

    # Активируем окошко
    WINDOW.activate()

    while True:
        shape_names: str = "\n"
        index = 1

        title = '►[1] VolumeShape\n►[2] AreaShape'
        try:
            shape_type = int(input("Выберите тип фигур с которыми вы хотите провести операцию:\n" + title + "\nВвод: "))

            if shapes.get(shape_type) is None:
                raise ValueError

            collection = shapes[shape_type]

            for shape in collection.values():
                shape_names += "► [" + str(index) + "] " + shape.__class__.__name__ + "\n"
                index += 1

            shape_id = int(input("Выберите фигур:" + shape_names + "Ввод: "))
            if collection.get(shape_id) is None:
                raise ValueError
            collection[shape_id].input_data()
        except ValueError:
            print("Введены не корректные данные.\nВводите только числовые значения.")
