"""
Defines the module with the unit test of rotines.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.util.rotines import requires, returns, implements
from pysocialsim.common.simulator.i_simulator import ISimulator
import pymockobject

import unittest

class RotinesTest(unittest.TestCase):
    
    def testRequires(self):
        self.assertTrue(requires("teste", str))
        self.assertRaises(TypeError, requires, 1, str)
        
    def testReturns(self):
        self.assertEquals("teste", returns("teste", str))
        self.assertRaises(TypeError, returns, "teste", int)
        
    def testImplements(self):
        self.assertTrue(implements(pymockobject.create(ISimulator), ISimulator))
        self.assertRaises(TypeError, implements,1, ISimulator)