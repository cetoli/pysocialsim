from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class PushOpportunitySimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "PUSH_OPPORTUNITY", peerId, priority)