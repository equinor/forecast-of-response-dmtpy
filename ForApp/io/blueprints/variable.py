# 
# Generated with VariableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class VariableBlueprint(Blueprint):
    """"""

    def __init__(self, name="Variable", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("value","string",""))
        self.attributes.append(Attribute("valueType","string",""))
        self.attributes.append(Attribute("unit","string",""))