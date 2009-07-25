from pysocialsim.simulator.i_simulator import ISimulator
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.base.interface import implements
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.simulator.event.i_event import IEvent
from pymockobject.events import ReturnValue
from pysocialsim.simulator.simulation.stochastic.default_stochastic_simulation import DefaultStochasticSimulation
from pysocialsim.simulator.simulation.stochastic.i_stochastic_simulation import IStochasticSimulation
from pysocialsim.simulator.simulation.stochastic.i_stochastic_model import IStochasticModel
import pymockobject
import unittest

class DefaultStochasticSimulationTest(unittest.TestCase):
    
    def setUp(self):
        self.__simulator = pymockobject.create(ISimulator)
        self.__network = pymockobject.create(IP2PNetwork)
        self.__simulation = DefaultStochasticSimulation(self.__simulator, self.__network)
    
    def test_implements_interface(self):
        self.assertTrue(implements(self.__simulation, ISimulation, IStochasticSimulation))
        self.assertEquals(self.__network, self.__simulation.getP2PNetwork())
    
    def test_register_events(self):
        event1 = pymockobject.create(IEvent)
        event1.getPriority.will(ReturnValue(1))
        
        event2 = pymockobject.create(IEvent)
        event2.getPriority.will(ReturnValue(2))
        
        event3 = pymockobject.create(IEvent)
        event3.getPriority.will(ReturnValue(3))
        
        self.assertEquals(event3, self.__simulation.registerEvent(event3))
        self.assertEquals(1, self.__simulation.countEvents())
        
        self.assertEquals(event1, self.__simulation.registerEvent(event1))
        self.assertEquals(2, self.__simulation.countEvents())
        
        self.assertEquals(event2, self.__simulation.registerEvent(event2))
        self.assertEquals(3, self.__simulation.countEvents())
        
        self.assertRaises(TypeError, self.__simulation.registerEvent, None)
        self.assertRaises(TypeError, self.__simulation.registerEvent, 1)
        self.assertRaises(TypeError, self.__simulation.registerEvent, False)
        self.assertRaises(TypeError, self.__simulation.registerEvent, True)
        self.assertRaises(TypeError, self.__simulation.registerEvent, "event")
        self.assertRaises(TypeError, self.__simulation.registerEvent, 0.6)
        
    def test_unregister_events(self):
        event1 = pymockobject.create(IEvent)
        event1.getPriority.will(ReturnValue(1))
        
        event2 = pymockobject.create(IEvent)
        event2.getPriority.will(ReturnValue(2))
        
        event3 = pymockobject.create(IEvent)
        event3.getPriority.will(ReturnValue(3))
        
        self.assertEquals(event3, self.__simulation.registerEvent(event3))
        self.assertEquals(1, self.__simulation.countEvents())
        
        self.assertEquals(event1, self.__simulation.registerEvent(event1))
        self.assertEquals(2, self.__simulation.countEvents())
        
        self.assertEquals(event2, self.__simulation.registerEvent(event2))
        self.assertEquals(3, self.__simulation.countEvents())
        
        self.assertEquals(event1, self.__simulation.unregisterEvent())
        self.assertEquals(2, self.__simulation.countEvents())
        
        self.assertEquals(event2, self.__simulation.unregisterEvent())
        self.assertEquals(1, self.__simulation.countEvents())
        
        self.assertEquals(event3, self.__simulation.unregisterEvent())
        self.assertEquals(0, self.__simulation.countEvents())
        
        self.assertFalse(self.__simulation.unregisterEvent())
        
    def test_simulation_time(self):
        self.assertEquals(3600, self.__simulation.setSimulationTime(3600))
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        
        self.assertRaises(StandardError, self.__simulation.setSimulationTime, 0)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        self.assertRaises(StandardError, self.__simulation.setSimulationTime, -1)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        
        self.assertRaises(TypeError, self.__simulation.setSimulationTime, "3600")
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        self.assertRaises(TypeError, self.__simulation.setSimulationTime, True)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        self.assertRaises(TypeError, self.__simulation.setSimulationTime, False)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        self.assertRaises(TypeError, self.__simulation.setSimulationTime, 0.2)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        self.assertRaises(TypeError, self.__simulation.setSimulationTime, self.__simulation)
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        
    def test_add_stochastic_models(self):
        model1 = pymockobject.create(IStochasticModel)
        model2 = pymockobject.create(IStochasticModel)
        model3 = pymockobject.create(IStochasticModel)
        
        self.assertEquals(model1, self.__simulation.addStochasticModel(model1))
        self.assertEquals(1, self.__simulation.countStochasticModels())
        
        self.assertEquals(model2, self.__simulation.addStochasticModel(model2))
        self.assertEquals(2, self.__simulation.countStochasticModels())
        
        self.assertEquals(model3, self.__simulation.addStochasticModel(model3))
        self.assertEquals(3, self.__simulation.countStochasticModels())
        
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, None)
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, 1)
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, 0.2)
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, "model")
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, True)
        self.assertRaises(TypeError, self.__simulation.addStochasticModel, False)
        
#        self.assertRaises(StandardError, self.__simulation.addStochasticModel, model1)
#        self.assertEquals(3, self.__simulation.countStochasticModels())
#        self.assertRaises(StandardError, self.__simulation.addStochasticModel, model2)
#        self.assertEquals(3, self.__simulation.countStochasticModels())
#        self.assertRaises(StandardError, self.__simulation.addStochasticModel, model3)
#        self.assertEquals(3, self.__simulation.countStochasticModels())

    def test_remove_stochastic_models(self):
        model1 = pymockobject.create(IStochasticModel)
        model2 = pymockobject.create(IStochasticModel)
        model3 = pymockobject.create(IStochasticModel)
        
        self.assertEquals(model1, self.__simulation.addStochasticModel(model1))
        self.assertEquals(1, self.__simulation.countStochasticModels())
        
        self.assertEquals(model2, self.__simulation.addStochasticModel(model2))
        self.assertEquals(2, self.__simulation.countStochasticModels())
        
        self.assertEquals(model3, self.__simulation.addStochasticModel(model3))
        self.assertEquals(3, self.__simulation.countStochasticModels())
        
        self.assertEquals(model1, self.__simulation.removeStochasticModel(model1))
        self.assertEquals(2, self.__simulation.countStochasticModels())
        
        self.assertEquals(model2, self.__simulation.removeStochasticModel(model2))
        self.assertEquals(1, self.__simulation.countStochasticModels())
        
        self.assertEquals(model3, self.__simulation.removeStochasticModel(model3))
        self.assertEquals(0, self.__simulation.countStochasticModels())
        
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, None)
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, 1)
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, 0.2)
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, "model")
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, True)
        self.assertRaises(TypeError, self.__simulation.removeStochasticModel, False)
        
    def test_execute(self):
        model1 = pymockobject.create(IStochasticModel)
        model1.generateEvents.expects(self.__simulation).will(ReturnValue(100))
        
        model2 = pymockobject.create(IStochasticModel)
        model2.generateEvents.expects(self.__simulation).will(ReturnValue(50))
        
        model3 = pymockobject.create(IStochasticModel)
        model3.generateEvents.expects(self.__simulation).will(ReturnValue(50))
        
        self.assertEquals(model1, self.__simulation.addStochasticModel(model1))
        self.assertEquals(1, self.__simulation.countStochasticModels())
        
        self.assertEquals(model2, self.__simulation.addStochasticModel(model2))
        self.assertEquals(2, self.__simulation.countStochasticModels())
        
        self.assertEquals(model3, self.__simulation.addStochasticModel(model3))
        self.assertEquals(3, self.__simulation.countStochasticModels())
        
        self.assertEquals(3600, self.__simulation.setSimulationTime(3600))
        self.assertEquals(3600, self.__simulation.getSimulationTime())
        
        self.__simulation.execute()
        
        self.assertEquals(720000, self.__simulation.getGeneratedEvents())
        