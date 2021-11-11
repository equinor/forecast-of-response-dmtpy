# 
# Generated with SimulationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class SimulationBlueprint(Blueprint):
    """"""

    def __init__(self, name="Simulation", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("progress","string",""))
        self.attributes.append(Attribute("simaJob","string",""))
        self.attributes.append(Attribute("started","string",""))
        self.attributes.append(BlueprintAttribute("result","/io/ResultFile","",False))
        self.attributes.append(Attribute("ended","string",""))