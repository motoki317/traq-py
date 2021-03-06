"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.webrtc_api import WebrtcApi  # noqa: E501


class TestWebrtcApi(unittest.TestCase):
    """WebrtcApi unit test stubs"""

    def setUp(self):
        self.api = WebrtcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_web_rtc_state(self):
        """Test case for get_web_rtc_state

        WebRTC状態を取得  # noqa: E501
        """
        pass

    def test_post_web_rtc_authenticate(self):
        """Test case for post_web_rtc_authenticate

        Skyway用認証API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
