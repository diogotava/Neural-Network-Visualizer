from Src.Layers.Layer import Layer
from Src.Utils.DrawShapes import *


class Conv2D(Layer):
    def __init__(self, shape, x_position, layer) -> None:
        color = [1.0, 0.5, 0.0, 1.0]

        Layer.__init__(self, color, shape, x_position, layer)
        pass

    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, self.color)
        self.center_position[0] = cube(self.shape, self.center_position[0])
        return self.center_position[0]

    def draw_color(self, color_code):
        glColor4f(color_code[0], color_code[1], color_code[2], color_code[3])
        self.center_position[0] = cube(self.shape, self.center_position[0])
        return self.center_position[0]
