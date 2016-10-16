import unittest
import ConfigParser
from dbconnection.DBConnection import DBConnection
from sites.Site import Site

class TestSite(unittest.TestCase):

  def setUp(self):
      self.site_info_without_priority = {'url':'yahyaqandel.com','name':'YahyaQandel','title':'Yahya Adel Qandel'}
      self.site_info_invalid_url = {'url':'http://zadgxe.com','name':'YahyaQandel','title':'Yahya Adel Qandel','priority':'5'}
      self.site_info = {'url': 'http://yahyaqandel.com', 'name': 'YahyaQandel', 'title': 'Yahya Adel Qandel',
                    'priority': '5'}
      self.test_db = None

  def test_site_object_not_null(self):
      site_obj = Site(self.site_info)
      self.assertIsNotNone(site_obj)

  def test_site_prioity_ignored(self):
      site_obj = Site(self.site_info_without_priority)
      self.assertEqual(site_obj.site_info['priority'],1)


  def test_site_invalid_url(self):
      site_obj = Site(self.site_info_invalid_url)
      self.assertRaises(Exception, site_obj.check_code_status)


  def test_site_valid_url(self):
      site_obj = Site(self.site_info)
      self.assertEqual(200, site_obj.check_code_status())

  def test_site_save(self):
      config = ConfigParser.ConfigParser()
      config.read('Configuration.cfg')
      self.test_db = config.get('DataDB', 'DBNAME_TEST')
      site_test_obj = Site(self.site_info,self.test_db)
      site_test_obj.save()
      client = DBConnection().client
      sites_collection = config.get('DataDB', 'SITES_COLLECTION')
      collection = client[self.test_db][sites_collection]
      sites_query = collection.find(
          {"title": self.site_info['title']}
      )
      self.assertEqual(sites_query.count(),1)

  def tearDown(self):
      if self.test_db:
          client = DBConnection().client
          client.drop_database(self.test_db)
