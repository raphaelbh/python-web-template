import unittest
from app.services import fake_service

class FakeServiceTest(unittest.TestCase):

    def test_fake_service(self):
        assert fake_service.execute() == "fake"

if __name__ == '__main__':
    unittest.main()