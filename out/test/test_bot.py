"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import traq
from traq.model.bot_mode import BotMode
from traq.model.bot_state import BotState
globals()['BotMode'] = BotMode
globals()['BotState'] = BotState
from traq.model.bot import Bot


class TestBot(unittest.TestCase):
    """Bot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBot(self):
        """Test Bot"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Bot()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
