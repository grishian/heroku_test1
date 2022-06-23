from app import app
import unittest


class FlaskTest(unittest.TestCase):

    # check for response 200

    def test_home(self):
        tester = app.test_client(self)
        ressponse = tester.get('/' or '/index')
        status_code = ressponse.status_code
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
