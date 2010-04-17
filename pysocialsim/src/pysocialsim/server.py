'''
Created on 17/04/2010

@author: Fabricio
'''
from pysocialsim.remote.master_node import MasterNode
from pysocialsim.p2p.network.peer_to_peer_network_remote_object import PeerToPeerNetworkRemoteObject

if __name__ == '__main__':
    masterNode = MasterNode()
    masterNode.start()
    masterNode.registerRemoteObject(PeerToPeerNetworkRemoteObject(), "network")