from viktor.parametrization import Parametrization, Section, NumberField, OptionField


class LogoParametrization(Parametrization):
    geometry = Section('Geometry')
    geometry.beam_length = NumberField('Length', suffix='mm', default=2000)

    material = Section('Material')
    material.density = NumberField('Density', suffix='kg/m3', default=8050)

    visualization = Section('Visualization')
    visualization.color = OptionField("Color", options=['Black', 'Blue', 'Yellow'], default='Yellow')
