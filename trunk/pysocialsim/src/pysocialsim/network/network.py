from pysocialsim.base.interface import Interface
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator

class Network(EventGenerator):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()