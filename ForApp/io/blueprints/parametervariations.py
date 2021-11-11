# 
# Generated with ParameterVariationsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ParameterVariationsBlueprint(Blueprint):
    """"""

    def __init__(self, name="ParameterVariations", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("variableRuns","/io/VariableRun","uncontained list of variable runs",False,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("parameters","/io/Variable","the variable value is a semi-colon separated list of parameters. Name and unit (and values) must correspond to the variables in the associated VariableRun",True))