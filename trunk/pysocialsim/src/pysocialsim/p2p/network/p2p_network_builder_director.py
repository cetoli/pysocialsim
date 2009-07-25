from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
import yaml

class P2PNetworkBuilderDirector(Object):
    
    def __init__(self, builder):
        self.__builder = builder
    
    @public
    def build(self, source, topology):
        conf = open(source, "r")
        params = yaml.load(conf)
        conf.close()
        print "Building network."
        self.__builder.createP2PNetwork(topology)
        self.__builder.buildP2PNetwork(params)
        print "Network done."       