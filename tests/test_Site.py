import unittest

from dbconnection.DBConnection import DBConnection
from sites.Site import Site

class TestSite(unittest.TestCase):

  def setUp(self):
      self.site_info_without_priority = {'url':'www.yahyaqandel.com','name':'YahyaQandel','title':'Yahya Adel Qandel'}
      self.site_info_invalid_url = {'url':'http://zsadf.com','name':'YahyaQandel','title':'Yahya Adel Qandel','priority':'5'}
      self.site_info = {'url': 'http://yahyaqandel.com', 'name': 'YahyaQandel', 'title': 'Yahya Adel Qandel',
                    'priority': '5'}

  def test_site_object_not_null(self):
      site_obj = Site(self.site_info)
      self.assertIsNotNone(site_obj)

  def test_site_save_prioity_ignored(self):
      site_obj = Site(self.site_info_without_priority)
      site_obj.save()
      self.assertEqual(site_obj.site_info['priority'],1)


  # def test_site_save_invalid_url(self):
  #     site_obj = Site(self.site_info_invalid_url)
  #     self.assertRaises(Exception, site_obj.save())

