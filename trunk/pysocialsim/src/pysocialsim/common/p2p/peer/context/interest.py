"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.common.p2p.peer.context.abstract_context import AbstractContext
from pysocialsim.common.p2p.peer.context.i_context import IContext

class Interest(AbstractContext):

    def __init__(self, id):
        AbstractContext.initialize(self, IContext.INTEREST, id)
        