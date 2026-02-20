# test_sushichef.py
"""
Tests for SushiChef module.
"""

import unittest
from sushichef import SushiChef

class TestSushiChef(unittest.TestCase):
    """Test cases for SushiChef class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SushiChef()
        self.assertIsInstance(instance, SushiChef)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SushiChef()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
