from pymongo import MongoClient
import urllib2

class Site(object):
    def __init__(self,site_info):
        self.site_info = site_info
        self.save()

    def save(self):
        site_dict = self.site_info
        if not 'priority' in site_dict:
            site_priority = {'priority':1}
            site_dict.update(site_priority)

        print site_dict['url']
            # print site_dict
        try:
            urllib2.urlopen(site_dict['url'])
            print site_dict['url']
            print conn
            conn.request("HEAD", "/")
            r1 = conn.getresponse()
            print r1
        except Exception as exc:
            raise Exception('Invalid site url')
