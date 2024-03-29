"""
Defines the module with the PeerToPeerMessageDispatcher class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""
from threading import Thread, Semaphore
from bisect import insort
from pysocialsim.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage

class PeerToPeerMessageDispatcher(object):
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
        self.__queues = {"EXIT": self.PriorityQueue()}
        self.__thread = None
        
    
        
    def registerPeerToPeerMessageHandler(self, peerToPeerMessageHandler):
        """
        Registers a handler for treating peer-to-peer messages.
        @param peerToPeerMessageHandler: an IPeerToPeerMessageHandler
        @type peerToPeerMessageHandler: IPeerToPeerMessageHandler
        @return: Returns True, if peer-to-peer message handler was registered in dispatcher. Else, returns False.
        @rtype: IPeerToPeerMessageHandler
        """
        if self.__peerToPeerMessageHandlers.has_key(peerToPeerMessageHandler.getHandle()):
            return False
        
        self.__peerToPeerMessageHandlers[peerToPeerMessageHandler.getHandle()] = peerToPeerMessageHandler
        self.__queues[peerToPeerMessageHandler.getHandle()] = self.PriorityQueue()
        return self.__peerToPeerMessageHandlers.has_key(peerToPeerMessageHandler.getHandle())
    
    
    def unregisterPeerToPeerMessageHandler(self, handle):
        """
        Unregisters a handler registered in peer-to-peer message dispatcher.
        @param handle: handle of peer-to-peer message handler.
        @return: Returns True, if peer-to-peer message handler was unregistered from the dispatcher. Else, False.
        @rtype: bool
        """
        if not self.__peerToPeerMessageHandlers.has_key(handle):
            return False
        
        del self.__peerToPeerMessageHandlers[handle]
        del self.__queues[handle]
        return not self.__peerToPeerMessageHandlers.has_key(handle)
    
    
    def countPeerToPeerMessageHandler(self):
        """
        Count the number of peer-to-peer message handlers.
        @return: an int
        @rtype: int
        """
        return len(self.__peerToPeerMessageHandlers)
    
    
    def handlePeerToPeerMessage(self, peerToPeerMessage):
        """
        Handles a peer-to-peer message.
        @param peerToPeerMessage: an IPeerToPeerMessage
        @type peerToPeerMessage: IPeerToPeerMessage
        @return: IPeerToPeerMessage
        """
        handlerClone = self.__peerToPeerMessageHandlers[peerToPeerMessage.getHandle()].clone()
        handlerClone.init(self.__peer)
        
        handlerClone.handlePeerToPeerMessage(peerToPeerMessage)
               
        return peerToPeerMessage
    
    
    def registerPeerToPeerMessage(self, peerToPeerMessage):
        self.__queues[peerToPeerMessage.getHandle()].enqueue(peerToPeerMessage, peerToPeerMessage.getPriority())
        self.__thread.__init__(self)
        
        
    def unregisterPeerToPeerMessage(self, handle):
        queue = self.__queues[handle]
        if queue.size() == 0:
            return None
        msg = queue.dequeue()
        return msg
    
    
    def countPeerToPeerMessages(self, handle):
        return self.__queues[handle]._qsize()
    
    
    def getPeerToPeerMessageHandles(self):
        return self.__queues.keys()
    
    
    def on(self):
        if self.__thread:
            self.__thread.__init__(self)
        self.__thread = self.PeerToPeerMessageHandlingThread(self)
        self.__thread.start()
        
    
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
                    for i in range(10):
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
            
    
    class PriorityQueue(object):
        
        def initialize(self):
            self.__queue = []
            
        
        def enqueue(self, item, priority):
            sem = Semaphore()
            sem.acquire()
            for message in self.__queue:
                if message[1] == item:
                    return None
            insort(self.__queue, (priority, item))
            sem.release()
            return item
        
        
        def dequeue(self):
            """
            Dequeues a simulation event.
            @return: an ISimulationEvent
            @rtype: ISimulationEvent
            """
            sem = Semaphore()
            sem.acquire()
            if len(self.__queue) == 0:
                sem.release()
                return None
            item = self.__queue.pop(0)[1]
            sem.release()
            return item
        
        
        def size(self):
            """
            Returns the size of queue.
            @return: an int
            @rtype: int
            """
            sem = Semaphore()
            sem.acquire()
            size = len(self.__queue)
            sem.release()
            return size
        
        
        def getFirst(self):
            """
            Gets the first simulation event of queue.
            @return: an ISimulationEvent
            @rtype: ISimulationEvent
            """
            sem = Semaphore()
            sem.acquire()
            if len(self.__queue) == 0:
                sem.release()
                return
            first = self.__queue[0]
            sem.release()
            return first[1]
        
        
        def getLast(self):
            """
            Gets the first simulation event of queue.
            @return: an ISimulationEvent
            @rtype: ISimulationEvent
            """
            sem = Semaphore()
            sem.acquire()
            if len(self.__queue) == 0:
                sem.release()
                return
            last = self.__queue[len(self.__queue) - 1]
            sem.release()
            return last[1]
        
        
        def clear(self):
            """
            Clean the queue of simulation events.
            @rtype: NoneType
            """
            del self.__queue
            self.__queue = []