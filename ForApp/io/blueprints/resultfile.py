# 
# Generated with ResultFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ResultFileBlueprint(Blueprint):
    """"""

    def __init__(self, name="ResultFile", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("variableRuns","/io/VariableRun","Results relating to a set of variables",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("comparisonGroups","/io/ComparisonGroups","",True,Dimension("size","")))