# This an autogenerated file
# 
# Generated with ParameterVariations
from __future__ import annotations
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.parametervariations import ParameterVariationsBlueprint
from typing import Dict,Sequence,List
from ForApp.io.variable import Variable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ForApp.io.variablerun import VariableRun

class ParameterVariations(Entity):
    """
    
    
    Keyword arguments
    -----------------
    name : str 
         (default "")
    description : str 
         (default "")
    variableRuns : List[VariableRun] 
         uncontained list of variable runs
    parameters : Variable 
         the variable value is a semi-colon separated list of parameters. Name and unit (and values) must correspond to the variables in the associated VariableRun
    """

    def __init__(self , name:str="", description:str="", 
        variableRuns:List[VariableRun]=None, **kwargs):
        self.__name = name
        self.__description = description
        self.__variableRuns = list() if variableRuns is None else variableRuns
        self.__parameters = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ParameterVariationsBlueprint()


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
    def variableRuns(self) -> List[VariableRun]:
        """uncontained list of variable runs"""
        return self.__variableRuns

    @variableRuns.setter
    def variableRuns(self, value: List[VariableRun]):
        """Set variableRuns"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableRuns = value

    @property
    def parameters(self) -> Variable:
        """the variable value is a semi-colon separated list of parameters. Name and unit (and values) must correspond to the variables in the associated VariableRun"""
        return self.__parameters

    @parameters.setter
    def parameters(self, value: Variable):
        """Set parameters"""
        self.__parameters = value
