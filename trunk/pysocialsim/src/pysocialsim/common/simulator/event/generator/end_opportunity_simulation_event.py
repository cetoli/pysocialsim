from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class EndOpportunitySimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "END_OPPORTUNITY", peerId, priority)