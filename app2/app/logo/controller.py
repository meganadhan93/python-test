from math import cos, sin, pi

from viktor import Color
from viktor.core import ViktorController
from viktor.geometry import Group, Line, Point, RectangularExtrusion
from viktor.views import DataGroup, DataItem, GeometryAndDataResult, GeometryAndDataView, Summary

from .parametrization import LogoParametrization


class LogoController(ViktorController):
    label = 'Logo design'
    summary = Summary()
    parametrization = LogoParametrization

    @GeometryAndDataView('3D model', duration_guess=1)
    def visualize(self, params, **kwargs):
        """ Creates a 3D representation of the logo, along with a data component. """

        beam_length = params.geometry.beam_length

        # left beam
        x_end = beam_length * sin(20 * pi / 180)
        z_end = beam_length * cos(20 * pi / 180)
        point_start = Point(0, 0, 0)
        point_end = Point(-x_end, 0, z_end)
        left_line = Line(point_start, point_end)
        left_beam = RectangularExtrusion(width=100, height=100, line=left_line)

        # right beam
        point_end = Point(x_end, 0, z_end)
        right_line = Line(point_start, point_end)
        right_beam = RectangularExtrusion(width=100, height=100, line=right_line)

        # top beam
        point_start = Point(-x_end, 0, 1.1 * z_end)
        point_end = Point(x_end, 0, 1.1 * z_end)
        top_line = Line(point_start, point_end)
        top_beam = RectangularExtrusion(width=100, height=100, line=top_line)

        # bottom beam
        point_start = Point(-x_end, 0, -0.1 * z_end)
        point_end = Point(x_end, 0, -0.1 * z_end)
        bottom_line = Line(point_start, point_end)
        bottom_beam = RectangularExtrusion(width=100, height=100, line=bottom_line)

        geometries = [left_beam, right_beam, top_beam, bottom_beam]

        if params.visualization.color == 'Black':
            beam_color = Color(0, 0, 0)
        elif params.visualization.color == 'Blue':
            beam_color = Color(100, 130, 255)
        elif params.visualization.color == 'Yellow':
            beam_color = Color(255, 220, 0)
        else:
            raise ValueError

        mass = 0
        for beam in geometries:
            beam.material.color = beam_color
            mass += beam.inner_volume * params.material.density * 1e-09  # inner volume in [mm3]

        data = DataGroup(DataItem(label='Mass', value=mass, suffix='kg'))

        return GeometryAndDataResult(Group(geometries), data)
