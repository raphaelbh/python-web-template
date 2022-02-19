import unittest
from application.run import app

class ApiTest(unittest.TestCase):

    def test_fake_request(self):
        client = app.test_client(self)
        response = client.get('/api/v1/demo')
        assert response.status_code == 200, "Should return status code 200"

if __name__ == '__main__':
    unittest.main()