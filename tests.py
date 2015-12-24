import unittest
import os
from isarest import app


class BaseConverterTestCase(unittest.TestCase):
    """Base test case for testing the converters"""
    def setUp(self):
        self.app = app.test_client()
        self.test_data_zip = open(os.path.join(os.path.dirname(__file__), 'testdata/BII-S-3.zip'), 'rb').read()
        # self.test_data_json = open(os.path.join(os.path.dirname(__file__), 'testdata/BII-I-1.json'), 'rb').read()

    def tearDown(self):
        # TODO: Implement any cleanup code, if necessary (e.g. temporary files when uncompressing received zips)
        pass


# class TabToJsonConverterTests(BaseConverterTestCase):
#
#     def test_convert(self):
#         response = self.app.post(path='/api/v1/convert/tab-to-json', data=self.test_data_zip,
#                                  headers={'Content-Type': 'application/zip'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.mimetype, 'application/json')
#
#     def test_unsupported_content(self):
#         response = self.app.post(path='/api/v1/convert/tab-to-json', data=self.test_data_json,
#                                  headers={'Content-Type': 'application/json'})
#         self.assertEqual(response.status_code, 415)


# class JsonToTabConverterTests(BaseConverterTestCase):
#
#     def test_convert(self):
#         response = self.app.post(path='/convert/json-to-isatab', data=self.test_data_json,
#                                  headers={'Content-Type': 'application/json'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.mimetype, 'application/zip')
#
#     def test_unsupported_mimetype(self):
#         response = self.app.post(path='/convert/json-to-isatab', data=self.test_data_zip,
#                          headers={'Content-Type': 'application/zip'})
#         self.assertEqual(response.status_code, 415)


class TabToSraXmlConverterTests(BaseConverterTestCase):

    def test_convert(self):
        response = self.app.post(path='/api/v1/convert/tab-to-sra', data=self.test_data_zip,
                                 headers={'Content-Type': 'application/zip'})
        outfile = open('tmp/out.zip', 'w')
        content = response.get_data()
        outfile.write(content.decode())
        outfile.close()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/zip')

    # def test_unsupported_content(self):
    #     response = self.app.post(path='/convert/isatab-to-sra', data=self.test_data_json,
    #                              headers={'Content-Type': 'application/json'})
    #     self.assertEqual(response.status_code, 415)

if __name__ == '__main__':
    unittest.main()
