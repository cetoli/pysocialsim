from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.public import public

class AbstractSimulator(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("simulation", Simulation)
    def initialize(self, simulation):
        self.__simulation = simulation
        self.__simulation.setSimulator(self)
    
    @public    
    @return_type(None.__class__)
    @require("event", Event)
    def handleEvent(self, event):
        raise NotImplementedError()
    
    
    def setDispatcher(self, dispatcher):
        raise NotImplementedError()
    
    def getSimulation(self):
        raise NotImplementedError()
        
    