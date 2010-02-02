'''
Created on 02/02/2010

@author: fabricio
'''
import time
import sha

class ContentIdGenerator(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def generateId(self, peer):
        id = "urn:content:id:"
        id += sha.new(peer.getId() + str(time.time())).hexdigest()
        return id