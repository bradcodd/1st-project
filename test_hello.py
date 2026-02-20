import unittest
from hello import hello

class TestHello(unittest.TestCase):
    def test_returns_hello_world(self):
        self.assertEqual(hello(), "Hello world!")

if __name__ == "__main__":
    unittest.main()
