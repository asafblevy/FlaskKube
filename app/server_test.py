import unittest

from server import home

class FlaskTestCase(unittest.TestCase):

  # Check if response is 200
  def test_index(self):
    tester = app.test_client
    response = tester.get("/")
    statuscode = response.status_code
    self.assertEqual(statuscode, 200)

if __name__ == "__main__":
  unittest.main()
