# Configuration for operations
# Generated with ConfigBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ConfigBlueprint(Blueprint):
    """Configuration for operations"""

    def __init__(self, name="Config", package_path="ForApp/io", description="Configuration for operations"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("simaVersion","string",""))
        self.attributes.append(BlueprintAttribute("phases","/io/Phase","",True,Dimension("size","")))