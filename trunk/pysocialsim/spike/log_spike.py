"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
import sha
#rpool = RandomPool()
#
#privatekeyCMS = DSA.generate(512, rpool.get_bytes)
#privatekeyClient = DSA.generate(512, rpool.get_bytes)
#publickeyCMS = privatekeyCMS.publickey()
#publickeyClient = privatekeyClient.publickey()
#
#PWD = "CUZINHO"
#
#signed_PWD = privatekeyCMS.sign(sha.new("mane").hexdigest(),"")
#enc_PWD = publickeyClient.encrypt(sha.new("mane").hexdigest(),"")
#print "with publickeyClient encrypted AES-PWD:"
#print enc_PWD
#print "with privatekeyCMS signed AES-PWD:"
#print signed_PWD
#
#dec_PWD= privatekeyClient.decrypt(enc_PWD[0])
#print "identity check:\n",publickeyCMS.verify(dec_PWD,signed_PWD)
#print "decrypted PWD:\n",dec_PWD

#from Crypto.PublicKey import DSA
#rpool = RandomPool()
#
#K = "tatu"
#PWD = "paca"
#
#privatekeyCMS = DSA.generate(368, rpool.get_bytes)
#publickeyCMS = privatekeyCMS.publickey()
#signed_PWD = privatekeyCMS.sign(PWD,K)
#
#
#print "identity check:\n",publickeyCMS.verify(dec_PWD,signed_PWD)
#print "decrypted PWD from ELGAMAL:\n",dec_PWD

