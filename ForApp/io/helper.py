from dmt.dmt_writer import DMTWriter
from dmt.dmt_reader import DMTReader
from dmt.entity import Entity
from typing import Dict,Sequence,List
import json

class EntityWriter(DMTWriter):
    """
    Local class for writing entities
    """
    def write(self, models: Sequence[Entity], 
              filename: str, indent=0, src=None, dest=None):
        """Write entity to a file. Change package path if necessary 
        to facilitate sharing if blueprints of recipient are stored 
        at a different location to source. 

        Args:
            models (Sequence[Entity]): entity for export
            filename (str): name of file to export to
            indent (int, optional): LHS indentation on file. Defaults to 0.
            src ([type], optional): Source package of blueprint. Defaults to None.
            dest ([type], optional): Destination package of blueprint. Defaults to None.
        """
        with open(filename, 'w', encoding="utf-8") as fp:
            dict=self.to_dict(models)
            json.dump(dict,fp,indent=indent) 
        if dest is not None and src is not None: change_package_path(filename,src,dest)
            
class EntityReader(DMTReader):
    """ Local class for reading entities """
    def read(self, filename:str, src=None, dest="ForApp/io/") -> Entity:
        """read entity from a file. Change package path if necessary 
        to facilitate sharing if blueprints of recipient are stored 
        at a different location to source. 

        Args:
            filename (str): filename containing entity data
            src ([type], optional): Source package of blueprint. Defaults to None.
            dest ([type], optional): Destination package of blueprint. Defaults to ForApp/io.

        Returns:
            Entity: Entity
        """
        if src is not None: change_package_path(filename,src,dest)
        with open(filename, 'r',encoding="utf-8") as file: res=json.load(file)
        if src is not None: change_package_path(filename,dest,src)
        return self.from_dict(res)
        
def change_package_path(filename, src, dest):
    with open(filename, 'r', encoding="utf-8") as fp:
        lines = [line.replace(src, dest) for line in fp.readlines()]
    with open(filename, 'w', encoding="utf-8") as fp:
        fp.writelines(lines)