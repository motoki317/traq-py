"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import traq
from traq.model.channel_stats_stamp import ChannelStatsStamp
from traq.model.channel_stats_user import ChannelStatsUser
globals()['ChannelStatsStamp'] = ChannelStatsStamp
globals()['ChannelStatsUser'] = ChannelStatsUser
from traq.model.channel_stats import ChannelStats


class TestChannelStats(unittest.TestCase):
    """ChannelStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelStats(self):
        """Test ChannelStats"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelStats()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
