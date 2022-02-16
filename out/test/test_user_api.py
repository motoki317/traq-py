"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_tag(self):
        """Test case for add_user_tag

        ユーザーにタグを追加  # noqa: E501
        """
        pass

    def test_change_user_icon(self):
        """Test case for change_user_icon

        ユーザーのアイコン画像を変更します  # noqa: E501
        """
        pass

    def test_change_user_password(self):
        """Test case for change_user_password

        ユーザーのパスワードを変更  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        ユーザーを登録  # noqa: E501
        """
        pass

    def test_edit_user(self):
        """Test case for edit_user

        ユーザー情報を変更  # noqa: E501
        """
        pass

    def test_edit_user_tag(self):
        """Test case for edit_user_tag

        ユーザーのタグを編集  # noqa: E501
        """
        pass

    def test_get_direct_messages(self):
        """Test case for get_direct_messages

        ダイレクトメッセージのリストを取得  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        ユーザー詳細情報を取得  # noqa: E501
        """
        pass

    def test_get_user_dm_channel(self):
        """Test case for get_user_dm_channel

        DMチャンネル情報を取得  # noqa: E501
        """
        pass

    def test_get_user_icon(self):
        """Test case for get_user_icon

        ユーザーのアイコン画像を取得  # noqa: E501
        """
        pass

    def test_get_user_stats(self):
        """Test case for get_user_stats

        ユーザー統計情報を取得  # noqa: E501
        """
        pass

    def test_get_user_tags(self):
        """Test case for get_user_tags

        ユーザーのタグリストを取得  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        ユーザーのリストを取得  # noqa: E501
        """
        pass

    def test_post_direct_message(self):
        """Test case for post_direct_message

        ダイレクトメッセージを送信  # noqa: E501
        """
        pass

    def test_remove_user_tag(self):
        """Test case for remove_user_tag

        ユーザーからタグを削除します  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
