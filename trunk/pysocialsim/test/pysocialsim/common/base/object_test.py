"""
Defines the module with unit test of Object class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.base.object import Object

import unittest

class ObjectTest(unittest.TestCase):
    
    def testTryInstantiateObjectClass(self):
        self.assertRaises(NotImplementedError, Object)
        
    