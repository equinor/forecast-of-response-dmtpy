# 
# Generated with SimulationConfigBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class SimulationConfigBlueprint(Blueprint):
    """"""

    def __init__(self, name="SimulationConfig", package_path="ForApp/io", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(BlueprintAttribute("variables","/io/Variable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("simulations","/io/Simulation","",True,Dimension("size","")))
        self.attributes.append(Attribute("published","boolean",""))