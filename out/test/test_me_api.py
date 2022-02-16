"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import traq
from traq.api.me_api import MeApi  # noqa: E501


class TestMeApi(unittest.TestCase):
    """MeApi unit test stubs"""

    def setUp(self):
        self.api = MeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_my_star(self):
        """Test case for add_my_star

        チャンネルをスターに追加  # noqa: E501
        """
        pass

    def test_add_my_user_tag(self):
        """Test case for add_my_user_tag

        自分にタグを追加  # noqa: E501
        """
        pass

    def test_change_my_icon(self):
        """Test case for change_my_icon

        自分のアイコン画像を変更  # noqa: E501
        """
        pass

    def test_change_my_notify_citation(self):
        """Test case for change_my_notify_citation

        メッセージ引用通知の設定情報を変更  # noqa: E501
        """
        pass

    def test_change_my_password(self):
        """Test case for change_my_password

        自分のパスワードを変更  # noqa: E501
        """
        pass

    def test_edit_me(self):
        """Test case for edit_me

        自分のユーザー情報を変更  # noqa: E501
        """
        pass

    def test_edit_my_user_tag(self):
        """Test case for edit_my_user_tag

        自分のタグを編集  # noqa: E501
        """
        pass

    def test_get_me(self):
        """Test case for get_me

        自分のユーザー詳細を取得  # noqa: E501
        """
        pass

    def test_get_my_channel_subscriptions(self):
        """Test case for get_my_channel_subscriptions

        自分のチャンネル購読状態を取得  # noqa: E501
        """
        pass

    def test_get_my_external_accounts(self):
        """Test case for get_my_external_accounts

        外部ログインアカウント一覧を取得  # noqa: E501
        """
        pass

    def test_get_my_icon(self):
        """Test case for get_my_icon

        自分のアイコン画像を取得  # noqa: E501
        """
        pass

    def test_get_my_notify_citation(self):
        """Test case for get_my_notify_citation

        メッセージ引用通知の設定情報を取得  # noqa: E501
        """
        pass

    def test_get_my_qr_code(self):
        """Test case for get_my_qr_code

        QRコードを取得  # noqa: E501
        """
        pass

    def test_get_my_sessions(self):
        """Test case for get_my_sessions

        自分のログインセッションリストを取得  # noqa: E501
        """
        pass

    def test_get_my_stamp_history(self):
        """Test case for get_my_stamp_history

        スタンプ履歴を取得  # noqa: E501
        """
        pass

    def test_get_my_stars(self):
        """Test case for get_my_stars

        スターチャンネルリストを取得  # noqa: E501
        """
        pass

    def test_get_my_tokens(self):
        """Test case for get_my_tokens

        有効トークンのリストを取得  # noqa: E501
        """
        pass

    def test_get_my_unread_channels(self):
        """Test case for get_my_unread_channels

        未読チャンネルを取得  # noqa: E501
        """
        pass

    def test_get_my_user_tags(self):
        """Test case for get_my_user_tags

        自分のタグリストを取得  # noqa: E501
        """
        pass

    def test_get_my_view_states(self):
        """Test case for get_my_view_states

        自身のチャンネル閲覧状態一覧を取得  # noqa: E501
        """
        pass

    def test_get_user_settings(self):
        """Test case for get_user_settings

        ユーザー設定を取得  # noqa: E501
        """
        pass

    def test_link_external_account(self):
        """Test case for link_external_account

        外部ログインアカウントを紐付ける  # noqa: E501
        """
        pass

    def test_read_channel(self):
        """Test case for read_channel

        チャンネルを既読にする  # noqa: E501
        """
        pass

    def test_register_fcm_device(self):
        """Test case for register_fcm_device

        FCMデバイスを登録  # noqa: E501
        """
        pass

    def test_remove_my_star(self):
        """Test case for remove_my_star

        チャンネルをスターから削除します  # noqa: E501
        """
        pass

    def test_remove_my_user_tag(self):
        """Test case for remove_my_user_tag

        自分からタグを削除します  # noqa: E501
        """
        pass

    def test_revoke_my_session(self):
        """Test case for revoke_my_session

        セッションを無効化  # noqa: E501
        """
        pass

    def test_revoke_my_token(self):
        """Test case for revoke_my_token

        トークンの認可を取り消す  # noqa: E501
        """
        pass

    def test_set_channel_subscribe_level(self):
        """Test case for set_channel_subscribe_level

        チャンネル購読レベルを設定  # noqa: E501
        """
        pass

    def test_unlink_external_account(self):
        """Test case for unlink_external_account

        外部ログインアカウントの紐付けを解除  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()