"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.message_api import MessageApi  # noqa: E501


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self):
        self.api = MessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_message_stamp(self):
        """Test case for add_message_stamp

        スタンプを押す  # noqa: E501
        """
        pass

    def test_create_pin(self):
        """Test case for create_pin

        ピン留めする  # noqa: E501
        """
        pass

    def test_delete_message(self):
        """Test case for delete_message

        メッセージを削除  # noqa: E501
        """
        pass

    def test_edit_message(self):
        """Test case for edit_message

        メッセージを編集  # noqa: E501
        """
        pass

    def test_get_direct_messages(self):
        """Test case for get_direct_messages

        ダイレクトメッセージのリストを取得  # noqa: E501
        """
        pass

    def test_get_message(self):
        """Test case for get_message

        メッセージを取得  # noqa: E501
        """
        pass

    def test_get_message_clips(self):
        """Test case for get_message_clips

        自分のクリップを取得  # noqa: E501
        """
        pass

    def test_get_message_stamps(self):
        """Test case for get_message_stamps

        メッセージのスタンプリストを取得  # noqa: E501
        """
        pass

    def test_get_messages(self):
        """Test case for get_messages

        チャンネルメッセージのリストを取得  # noqa: E501
        """
        pass

    def test_get_pin(self):
        """Test case for get_pin

        ピン留めを取得  # noqa: E501
        """
        pass

    def test_post_direct_message(self):
        """Test case for post_direct_message

        ダイレクトメッセージを送信  # noqa: E501
        """
        pass

    def test_post_message(self):
        """Test case for post_message

        チャンネルにメッセージを投稿  # noqa: E501
        """
        pass

    def test_remove_message_stamp(self):
        """Test case for remove_message_stamp

        スタンプを消す  # noqa: E501
        """
        pass

    def test_remove_pin(self):
        """Test case for remove_pin

        ピン留めを外す  # noqa: E501
        """
        pass

    def test_search_messages(self):
        """Test case for search_messages

        メッセージを検索  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
