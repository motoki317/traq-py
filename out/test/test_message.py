"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import traq
from traq.model.message_stamp import MessageStamp
globals()['MessageStamp'] = MessageStamp
from traq.model.message import Message


class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessage(self):
        """Test Message"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Message()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
