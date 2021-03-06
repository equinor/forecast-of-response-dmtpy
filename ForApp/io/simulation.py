# This an autogenerated file
# 
# Generated with Simulation
from __future__ import annotations
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.simulation import SimulationBlueprint
from typing import Dict
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ForApp.io.resultfile import ResultFile

class Simulation(Entity):
    """
    
    
    Keyword arguments
    -----------------
    name : str 
         (default "")
    description : str 
         (default "")
    progress : str 
         (default "")
    simaJob : str 
         (default "")
    started : str 
         (default "")
    result : ResultFile 
         
    ended : str 
         (default "")
    """

    def __init__(self , name:str="", description:str="", progress:str="", simaJob:str="", started:str="", ended:str="", **kwargs):
        self.__name = name
        self.__description = description
        self.__progress = progress
        self.__simaJob = simaJob
        self.__started = started
        self.__result = None
        self.__ended = ended
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SimulationBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def progress(self) -> str:
        """"""
        return self.__progress

    @progress.setter
    def progress(self, value: str):
        """Set progress"""
        self.__progress = str(value)

    @property
    def simaJob(self) -> str:
        """"""
        return self.__simaJob

    @simaJob.setter
    def simaJob(self, value: str):
        """Set simaJob"""
        self.__simaJob = str(value)

    @property
    def started(self) -> str:
        """"""
        return self.__started

    @started.setter
    def started(self, value: str):
        """Set started"""
        self.__started = str(value)

    @property
    def result(self) -> ResultFile:
        """"""
        return self.__result

    @result.setter
    def result(self, value: ResultFile):
        """Set result"""
        self.__result = value

    @property
    def ended(self) -> str:
        """"""
        return self.__ended

    @ended.setter
    def ended(self, value: str):
        """Set ended"""
        self.__ended = str(value)
