"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.bot_api import BotApi  # noqa: E501


class TestBotApi(unittest.TestCase):
    """BotApi unit test stubs"""

    def setUp(self):
        self.api = BotApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_bot(self):
        """Test case for activate_bot

        BOTをアクティベート  # noqa: E501
        """
        pass

    def test_change_bot_icon(self):
        """Test case for change_bot_icon

        BOTのアイコン画像を変更  # noqa: E501
        """
        pass

    def test_connect_bot_ws(self):
        """Test case for connect_bot_ws

        WebSocket Mode BOT用通知ストリームに接続します  # noqa: E501
        """
        pass

    def test_create_bot(self):
        """Test case for create_bot

        BOTを作成  # noqa: E501
        """
        pass

    def test_delete_bot(self):
        """Test case for delete_bot

        BOTを削除  # noqa: E501
        """
        pass

    def test_edit_bot(self):
        """Test case for edit_bot

        BOT情報を変更  # noqa: E501
        """
        pass

    def test_get_bot(self):
        """Test case for get_bot

        BOT情報を取得  # noqa: E501
        """
        pass

    def test_get_bot_icon(self):
        """Test case for get_bot_icon

        BOTのアイコン画像を取得  # noqa: E501
        """
        pass

    def test_get_bot_logs(self):
        """Test case for get_bot_logs

        BOTのイベントログを取得  # noqa: E501
        """
        pass

    def test_get_bots(self):
        """Test case for get_bots

        BOTリストを取得  # noqa: E501
        """
        pass

    def test_get_channel_bots(self):
        """Test case for get_channel_bots

        チャンネル参加中のBOTのリストを取得  # noqa: E501
        """
        pass

    def test_inactivate_bot(self):
        """Test case for inactivate_bot

        BOTをインアクティベート  # noqa: E501
        """
        pass

    def test_let_bot_join_channel(self):
        """Test case for let_bot_join_channel

        BOTをチャンネルに参加させる  # noqa: E501
        """
        pass

    def test_let_bot_leave_channel(self):
        """Test case for let_bot_leave_channel

        BOTをチャンネルから退出させる  # noqa: E501
        """
        pass

    def test_reissue_bot(self):
        """Test case for reissue_bot

        BOTのトークンを再発行  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
