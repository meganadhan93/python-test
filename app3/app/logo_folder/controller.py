from viktor.core import ViktorController
from viktor.views import Summary


class LogoFolderController(ViktorController):
    label = 'Logo folder'
    summary = Summary()
    children = ['Logo']
    show_children_as = 'Cards'  # or 'Table'
