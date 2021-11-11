# 
# Generated with ComparisonGroupsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ComparisonGroupsBlueprint(Blueprint):
    """"""

    def __init__(self, name="ComparisonGroups", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("parameterVariations","/io/ParameterVariations","",True,Dimension("size","")))