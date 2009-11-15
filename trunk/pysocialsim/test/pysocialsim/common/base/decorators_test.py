"""
Defines the module with test implementations for decorators module.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.base.decorators import public

import unittest

class DecoratorsTest(unittest.TestCase):
    
    def testPublicDecorator(self):
        
        def aFunction():
            pass
        
        func = aFunction
        self.assertEquals(func, public(func))
        self.assertTrue(func.__public__)