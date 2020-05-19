# -*- coding: utf-8 -*-
import hashlib,base64,random,string

class UserService():

    @staticmethod
    def geneAuthCode(user_info = None ):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.id, user_info.email, user_info.passwd, user_info.salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

#生成密码
    @staticmethod
    def genePwd( pwd,salt):
        m = hashlib.md5()
        str = "%s-%s" % ( base64.encodebytes( pwd.encode("utf-8") ) , salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt( length = 16 ):
        keylist = [ random.choice( ( string.ascii_letters + string.digits ) ) for i in range( length ) ]
        return ( "".join( keylist ) )
