"""
Defines the module with the implementation of AbstractSimulationEventTest class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

import unittest

class AbstractSimulationEventTest(unittest.TestCase):
    
    def testTryInstantiateAbstractSimulation(self):
        self.assertRaises(NotImplementedError, AbstractSimulationEvent)