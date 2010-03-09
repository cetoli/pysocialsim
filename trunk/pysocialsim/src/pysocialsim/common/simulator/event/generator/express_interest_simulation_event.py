from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class ExpressInterestSimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "EXPRESS_INTEREST", peerId, priority)