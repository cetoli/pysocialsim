from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.dispatcher.dispatcher import Dispatcher
from types import NoneType

class AbstractSimulator(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("simulation", Simulation)
    def initialize(self, simulation):
        self.__simulation = simulation
        self.__simulation.setSimulator(self)
        self.__dispatcher = None
    
    @public    
    @return_type(Event)
    @require("event", Event)
    def handleEvent(self, event):
        return self.__dispatcher.handleEvent(event)
    
    @public
    @return_type(Dispatcher)
    @require("dispatcher", Dispatcher)
    def setDispatcher(self, dispatcher):
        self.__dispatcher = dispatcher
        return self.__dispatcher
    
    @public
    @return_type(Simulation)
    def getSimulation(self):
        return self.__simulation
    
    @public
    @return_type(NoneType)    
    def configure(self):
        self.__simulation.generateEvents()
    
    @public
    @return_type(NoneType)
    def execute(self):
        self.__simulation.simulate()
    
    @public
    @return_type(NoneType)
    def stop(self):
        self.__simulation.stop()