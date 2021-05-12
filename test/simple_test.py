import unittest
import utils

class TestAvailableModelUtilFunctions(unittest.TestCase):
    """This test suite tests the functions that give access to the config file"""

    def test_conf_exist(self):
        """This function tests if the config file for the translation server exists"""
        self.assertIsInstance(utils.get_env_var("FLASKKEY"), str, "get_env_var() could not find a flask Key")

    def test_get_conf(self):
        """This function tests if the get_conf function returns a dictionary with the config file"""
        self.assertIsInstance(utils.get_env_var("None"), str, "get_env_var")

