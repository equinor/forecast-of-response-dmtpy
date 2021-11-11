# Results from a simulation corresponding to a set of key:value variables (no variations)
# Generated with VariableRunBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class VariableRunBlueprint(Blueprint):
    """Results from a simulation corresponding to a set of key:value variables (no variations)"""

    def __init__(self, name="VariableRun", package_path="ForApp/io", description="Results from a simulation corresponding to a set of key:value variables (no variations)"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("responses","/io/Response","a list of responses, where each response can have a number of timeseries which relate to its statistics e.g. mean response, max response etc...",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("variables","/io/Variable","",True,Dimension("size","")))