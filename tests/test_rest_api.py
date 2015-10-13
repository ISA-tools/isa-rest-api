import unittest
import os
from isarestapi import run


class TestIsaApi(unittest.TestCase):

    def setUp(self):
        self.app = run.app.test_client()
        self.fileobj = open(os.path.join(os.path.dirname(__file__), 'data/BII-I-1.zip'), 'rb')
        json_fileobj = open(os.path.join(os.path.dirname(__file__), 'data/BII-I-1.json'), 'rb')
        self.json = json_fileobj.read()

    def tearDown(self):
        pass

    def test_convert_to_isajson(self):
        response = self.app.post(path='/convert/isatab-to-json', data={'file': (self.fileobj, 'BII-I-1.zip')},
                                 headers={'Content-Type': 'multipart/form-data'})
        assert(response.status_code == 200)
        assert(response.mimetype == 'application/json')
        # TODO Validate what's returned is correct based on what we sent
        print("Received " + str(len(response.data)) + " of JSON, OK")

    def test_convert_to_isatab(self):
        response = self.app.post(path='/convert/json-to-isatab', data=self.json, headers={'Content-Type': 'application/json'})
        assert(response.status_code == 200)
        assert(response.mimetype == 'application/zip')
        # TODO Validate what's returned is correct based on what we sent
        print("Received " + str(len(response.data)) + " of ZIP content, OK")

    def test_unsupported_mimetype(self):
        response = self.app.post(path='/convert/isatab-to-json', data={'file': (self.fileobj, 'BII-I-1.zip')},
                                 headers={'Content-Type': 'application/zip'})
        assert(response.status_code == 415)
        response = self.app.post(path='/convert/json-to-isatab', data={'file': (self.fileobj, 'BII-I-1.zip')},
                         headers={'Content-Type': 'application/zip'})
        assert(response.status_code == 415)


if __name__ == '__main__':
    unittest.main()
