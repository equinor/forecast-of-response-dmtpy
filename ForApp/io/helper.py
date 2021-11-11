from dmt.dmt_writer import DMTWriter
from dmt.dmt_reader import DMTReader
from dmt.entity import Entity
from typing import Dict,Sequence,List
import json

class EntityWriter(DMTWriter):
    """
    Local class for writing entities (move to ForApp.helper)
    """
    def write(self, models: Sequence[Entity], filename: str, indent=0):
        with open(filename, 'w', encoding="utf-8") as fp:
            dict=self.to_dict(models)
            json.dump(dict,fp,indent=indent) 
            
class EntityReader(DMTReader):
    """ Just a wrapper """
    pass