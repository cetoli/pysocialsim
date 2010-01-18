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
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from Queue import Queue
from threading import Thread, Semaphore
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage

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
        self.__queues = {"EXIT": Queue()}
        self.__thread = self.PeerToPeerMessageHandlingThread(self)
        
    
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
        self.__queues[peerToPeerMessageHandler.getHandle()] = Queue()
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
        del self.__queues[handle]
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
        
        handlerClone = self.__peerToPeerMessageHandlers[peerToPeerMessage.getHandle()].clone()
        handlerClone.init(self.__peer)
        
        handlerClone.handlePeerToPeerMessage(peerToPeerMessage)
               
        return peerToPeerMessage
    
    @public
    def registerPeerToPeerMessage(self, peerToPeerMessage):
        self.__queues[peerToPeerMessage.getHandle()].put(peerToPeerMessage)
        
    @public    
    def unregisterPeerToPeerMessage(self, handle):
        sem = Semaphore()
        sem.acquire()
        queue = self.__queues[handle]
        if queue.empty():
            sem.release()
            return None
        msg = queue.get()
        sem.release()
        queue.task_done()
        return msg
    
    @public
    def countPeerToPeerMessages(self, handle):
        return self.__queues[handle]._qsize()
    
    @public
    def getPeerToPeerMessageHandles(self):
        return self.__queues.keys()
    
    @public
    def on(self):
        self.__thread.start()
        
    @public
    def off(self):
        self.registerPeerToPeerMessage(self.ExitPeerToPeerMessage())
    
    class PeerToPeerMessageHandlingThread(Thread):
        
        def __init__(self, dispatcher):
            Thread.__init__(self)
            self.__dispatcher = dispatcher
            
        def run(self):
            on = True
            while on:
                for handle in self.__dispatcher.getPeerToPeerMessageHandles():
                    msg = self.__dispatcher.unregisterPeerToPeerMessage(handle)
                    
                    if not msg:
                        continue
                    
                    if msg.getHandle() == "EXIT":
                        on = False
                        break
                    
                    self.__dispatcher.handlePeerToPeerMessage(msg)
                
    class ExitPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.SYSTEM, "EXIT", 0)