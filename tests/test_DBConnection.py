import unittest

from dbconnection.DBConnection import DBConnection


class TestDBConnection(unittest.TestCase):

  def setUp(self):
        DBConnection.client = None

  def test_default_configuration(self):
      self.assertEqual(DBConnection().client.address,('localhost', 27017))


  def test_assigned_configuration(self):
    self.assertEqual(DBConnection('localhost', 27017).client.address, ('localhost', 27017))


  # def test_wrong_assigned_configuration(self):
  #   self.assertRaises(Exception,DBConnection,'myserver.com', 27019)
