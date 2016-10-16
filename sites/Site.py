import ConfigParser
from dbconnection.DBConnection import DBConnection
import httplib
import mechanize


class Site(object):
    def __init__(self,site_info,dbname="default"):
        self.site_info = site_info
        self._db=dbname
        if not 'priority' in self.site_info:
            site_priority = {'priority': 1}
            self.site_info.update(site_priority)

    def save(self):
        site_dict = self.site_info
        collection = self.setup_dbClient()
        sites_query = collection.find(
            {"title":site_dict['title']
            }
        )
        if sites_query.count()==0:
            collection.insert_one(site_dict)

    def setup_dbClient(self):
        config = ConfigParser.ConfigParser()
        config.read('Configuration.cfg')
        if self._db=="default":
            self._db = config.get('DataDB', 'DBNAME')
        client = DBConnection().client
        sites_collection = config.get('DataDB', 'SITES_COLLECTION')
        return client[self._db][sites_collection]

    def check_code_status(self):
        try:
            httplib.HTTPConnection.debuglevel = 1
            request = mechanize.Request(self.site_info['url'], headers={'User-Agent': 'Python-mechanize'})
            response = mechanize.urlopen(request)
            return response.code
        except Exception as exc:
            raise Exception('Invalid site url')
