"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/04/2010
"""
from pysocialsim.simulator.simulation.abstract_simulation import AbstractSimulation

class ConcreteSimulation(AbstractSimulation):

    def __init__(self):
        AbstractSimulation.initialize(self)
        