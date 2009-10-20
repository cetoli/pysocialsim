"""
Defines the module with the PeerToPeerMessageDispatcher class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
from threading import Thread, BoundedSemaphore
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from random import randint
import time

class PeerToPeerMessageDispatcher(Object):
    """
    Defines the implementation of dispatcher for peer-to-peer message.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 15/10/2009
    """

    def __init__(self, peer):
        self.initialize(peer)
    
    def initialize(self, peer):
        """
        Initializes the object.
        @param peer: an IPeer
        @type peer: IPeer
        """
        self.__peer = peer
        self.__peerToPeerMessageHandlers = {}
    
    @public    
    def registerPeerToPeerMessageHandler(self, peerToPeerMessageHandler):
        """
        Registers a handler for treating peer-to-peer messages.
        @param peerToPeerMessageHandler: an IPeerToPeerMessageHandler
        @type peerToPeerMessageHandler: IPeerToPeerMessageHandler
        @return: Returns True, if peer-to-peer message handler was registered in dispatcher. Else, returns False.
        @rtype: IPeerToPeerMessageHandler
        """
        requires(peerToPeerMessageHandler, IPeerToPeerMessageHandler)
        pre_condition(peerToPeerMessageHandler, lambda x: x <> None)
        if self.__peerToPeerMessageHandlers.has_key(peerToPeerMessageHandler.getHandle()):
            return False
        
        self.__peerToPeerMessageHandlers[peerToPeerMessageHandler.getHandle()] = peerToPeerMessageHandler
        return self.__peerToPeerMessageHandlers.has_key(peerToPeerMessageHandler.getHandle())
    
    @public
    def unregisterPeerToPeerMessageHandler(self, handle):
        """
        Unregisters a handler registered in peer-to-peer message dispatcher.
        @param handle: handle of peer-to-peer message handler.
        @return: Returns True, if peer-to-peer message handler was unregistered from the dispatcher. Else, False.
        @rtype: bool
        """
        requires(handle, str)
        pre_condition(handle, lambda x: x <> None)
        
        if not self.__peerToPeerMessageHandlers.has_key(handle):
            return False
        
        del self.__peerToPeerMessageHandlers[handle]
        return not self.__peerToPeerMessageHandlers.has_key(handle)
    
    @public
    def countPeerToPeerMessageHandler(self):
        """
        Count the number of peer-to-peer message handlers.
        @return: an int
        @rtype: int
        """
        return len(self.__peerToPeerMessageHandlers)
    
    @public
    def handlePeerToPeerMessage(self, peerToPeerMessage):
        """
        Handles a peer-to-peer message.
        @param peerToPeerMessage: an IPeerToPeerMessage
        @type peerToPeerMessage: IPeerToPeerMessage
        @return: IPeerToPeerMessage
        """
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: self.__peerToPeerMessageHandlers.has_key(x.getHandle()))
        
        try:
            pool = BoundedSemaphore(1)
            pool.acquire()
            handlerClone = self.__peerToPeerMessageHandlers[peerToPeerMessage.getHandle()].clone()
            handlerClone.init(self.__peer)
            threadHandling = self.PeerToPeerMessageHandlingThread(handlerClone, peerToPeerMessage)
            threadHandling.start()
            threadHandling.join()
            pool.release()
        except:
            time.sleep(1)
            print 333333333333333333333333333 
            self.handlePeerToPeerMessage(peerToPeerMessage)
               
        return peerToPeerMessage
    
    class PeerToPeerMessageHandlingThread(Thread):
        
        def __init__(self, handler, message):
            Thread.__init__(self)
            self.__handler = handler
            self.__message = message
            
        def run(self):
            self.__handler.handlePeerToPeerMessage(self.__message)
    
    