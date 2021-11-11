# Generated with PlotTypes
# 
from enum import Enum
from enum import auto

class PlotTypes(Enum):
    """"""
    line = auto()
    arrow = auto()
    shaded = auto()

    def label(self):
        if self == PlotTypes.line:
            return "line"
        if self == PlotTypes.arrow:
            return "arrow"
        if self == PlotTypes.shaded:
            return "shaded"