"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import traq
from traq.model.file_info_thumbnail import FileInfoThumbnail
from traq.model.thumbnail_info import ThumbnailInfo
globals()['FileInfoThumbnail'] = FileInfoThumbnail
globals()['ThumbnailInfo'] = ThumbnailInfo
from traq.model.file_info import FileInfo


class TestFileInfo(unittest.TestCase):
    """FileInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFileInfo(self):
        """Test FileInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FileInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()