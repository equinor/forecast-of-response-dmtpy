# Storage for a single response time series e.g. Significant wave height vs time
# Generated with TimeseriesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class TimeseriesBlueprint(Blueprint):
    """Storage for a single response time series e.g. Significant wave height vs time"""

    def __init__(self, name="Timeseries", package_path="ForApp/io", description="Storage for a single response time series e.g. Significant wave height vs time"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("datetimes","string","datetimes from Unix epoch \n(Jan 1st 1970 at 00:00:00 UTC)",Dimension("size","")))
        self.attributes.append(Attribute("values","number","The value array corresponding to the datetimes",Dimension("size","")))
        self.attributes.append(Attribute("unit","string","The unit of the values"))
        self.attributes.append(BlueprintAttribute("threshold","/io/Threshold","Optional threshold",True))
        self.attributes.append(EnumAttribute("plotType","string",""))