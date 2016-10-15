from pymongo import MongoClient, errors
import ConfigParser
class DBConnection:
    class DBClient:
        def __init__(self,host,port):
            config = ConfigParser.ConfigParser()
            config.read('Configuration.cfg')
            if not host:
                self.host= config.get('MongoDBCred', 'host')
            else:
                self.host=host
            if not port:
                self.port = config.get('MongoDBCred', 'port')
            else:
                self.port = port
            self.client = MongoClient("mongodb://%s:%s" % (self.host, self.port))
            try:
                self.test = self.client.address
            except errors.ServerSelectionTimeoutError as inst:
                raise Exception('Cannot connect to host %s'%(self.host))

    client = None

    def __init__(self,host=None,port=None):
        if not DBConnection.client:
            DBConnection.client = DBConnection.DBClient(host,port).client

