from pysocialsim.simulator.dispatcher.abstract_dispatcher import AbstractDispatcher

class DefaultDispatcher(AbstractDispatcher):
    
    def __init__(self, simulator):
        self.initialize(simulator)