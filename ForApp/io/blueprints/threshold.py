# 
# Generated with ThresholdBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ThresholdBlueprint(Blueprint):
    """"""

    def __init__(self, name="Threshold", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("max","number",""))
        self.attributes.append(Attribute("min","number",""))
        self.attributes.append(Attribute("unit","string",""))