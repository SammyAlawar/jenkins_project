import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World from Sammy Alawar!"), "Hello, World from Sammy Alawar!")
if __name__ == "__main__":
    unittest.main()
