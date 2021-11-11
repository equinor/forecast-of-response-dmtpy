# A phase belonging to an Operation
# Generated with PhaseBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class PhaseBlueprint(Blueprint):
    """A phase belonging to an Operation"""

    def __init__(self, name="Phase", package_path="ForApp/io", description="A phase belonging to an Operation"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("simulationConfigs","/io/SimulationConfig","",True,Dimension("size","")))
        self.attributes.append(Attribute("start","string",""))
        self.attributes.append(Attribute("workflowTask","string",""))
        self.attributes.append(Attribute("end","string",""))
        self.attributes.append(Attribute("status","string",""))
        self.attributes.append(BlueprintAttribute("defaultVariables","/io/Variable","",True,Dimension("size","")))