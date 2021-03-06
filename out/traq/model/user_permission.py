"""
    traQ v3

    traQ v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from traq.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from traq.exceptions import ApiAttributeError



class UserPermission(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'GetWebhook': "get_webhook",
            'CreateWebhook': "create_webhook",
            'EditWebhook': "edit_webhook",
            'DeleteWebhook': "delete_webhook",
            'AccessOthersWebhook': "access_others_webhook",
            'GetBot': "get_bot",
            'CreateBot': "create_bot",
            'EditBot': "edit_bot",
            'DeleteBot': "delete_bot",
            'AccessOthersBot': "access_others_bot",
            'BotActionJoinChannel': "bot_action_join_channel",
            'BotActionLeaveChannel': "bot_action_leave_channel",
            'CreateChannel': "create_channel",
            'GetChannel': "get_channel",
            'EditChannel': "edit_channel",
            'DeleteChannel': "delete_channel",
            'ChangeParentChannel': "change_parent_channel",
            'EditChannelTopic': "edit_channel_topic",
            'GetChannelStar': "get_channel_star",
            'EditChannelStar': "edit_channel_star",
            'GetMyTokens': "get_my_tokens",
            'RevokeMyToken': "revoke_my_token",
            'GetClients': "get_clients",
            'CreateClient': "create_client",
            'EditMyClient': "edit_my_client",
            'DeleteMyClient': "delete_my_client",
            'ManageOthersClient': "manage_others_client",
            'UploadFile': "upload_file",
            'DownloadFile': "download_file",
            'DeleteFile': "delete_file",
            'GetMessage': "get_message",
            'PostMessage': "post_message",
            'EditMessage': "edit_message",
            'DeleteMessage': "delete_message",
            'ReportMessage': "report_message",
            'GetMessageReports': "get_message_reports",
            'CreateMessagePin': "create_message_pin",
            'DeleteMessagePin': "delete_message_pin",
            'GetChannelSubscription': "get_channel_subscription",
            'EditChannelSubscription': "edit_channel_subscription",
            'ConnectNotificationStream': "connect_notification_stream",
            'RegisterFCMDevice': "register_fcm_device",
            'GetStamp': "get_stamp",
            'CreateStamp': "create_stamp",
            'EditStamp': "edit_stamp",
            'EditStampCreatedByOthers': "edit_stamp_created_by_others",
            'DeleteStamp': "delete_stamp",
            'AddMessageStamp': "add_message_stamp",
            'RemoveMessageStamp': "remove_message_stamp",
            'GetMyStampHistory': "get_my_stamp_history",
            'GetStampPalette': "get_stamp_palette",
            'CreateStampPalette': "create_stamp_palette",
            'EditStampPalette': "edit_stamp_palette",
            'DeleteStampPalette': "delete_stamp_palette",
            'GetUser': "get_user",
            'RegisterUser': "register_user",
            'GetMe': "get_me",
            'EditMe': "edit_me",
            'ChangeMyIcon': "change_my_icon",
            'ChangeMyPassword': "change_my_password",
            'EditOtherUsers': "edit_other_users",
            'GetUserQRCode': "get_user_qr_code",
            'GetUserTag': "get_user_tag",
            'EditUserTag': "edit_user_tag",
            'GetUserGroup': "get_user_group",
            'CreateUserGroup': "create_user_group",
            'CreateSpecialUserGroup': "create_special_user_group",
            'EditUserGroup': "edit_user_group",
            'DeleteUserGroup': "delete_user_group",
            'AllUserGroupsAdmin': "edit_others_user_group",
            'WebRTC': "web_rtc",
            'GetMySessions': "get_my_sessions",
            'DeleteMySessions': "delete_my_sessions",
            'GetMyExternalAccount': "get_my_external_account",
            'EditMyExternalAccount': "edit_my_external_account",
            'GetUnread': "get_unread",
            'DeleteUnread': "delete_unread",
            'GetClipFolder': "get_clip_folder",
            'CreateClipFolder': "create_clip_folder",
            'EditClipFolder': "edit_clip_folder",
            'DeleteClipFolder': "delete_clip_folder",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """UserPermission - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): ??????????????????., must be one of ["get_webhook", "create_webhook", "edit_webhook", "delete_webhook", "access_others_webhook", "get_bot", "create_bot", "edit_bot", "delete_bot", "access_others_bot", "bot_action_join_channel", "bot_action_leave_channel", "create_channel", "get_channel", "edit_channel", "delete_channel", "change_parent_channel", "edit_channel_topic", "get_channel_star", "edit_channel_star", "get_my_tokens", "revoke_my_token", "get_clients", "create_client", "edit_my_client", "delete_my_client", "manage_others_client", "upload_file", "download_file", "delete_file", "get_message", "post_message", "edit_message", "delete_message", "report_message", "get_message_reports", "create_message_pin", "delete_message_pin", "get_channel_subscription", "edit_channel_subscription", "connect_notification_stream", "register_fcm_device", "get_stamp", "create_stamp", "edit_stamp", "edit_stamp_created_by_others", "delete_stamp", "add_message_stamp", "remove_message_stamp", "get_my_stamp_history", "get_stamp_palette", "create_stamp_palette", "edit_stamp_palette", "delete_stamp_palette", "get_user", "register_user", "get_me", "edit_me", "change_my_icon", "change_my_password", "edit_other_users", "get_user_qr_code", "get_user_tag", "edit_user_tag", "get_user_group", "create_user_group", "create_special_user_group", "edit_user_group", "delete_user_group", "edit_others_user_group", "web_rtc", "get_my_sessions", "delete_my_sessions", "get_my_external_account", "edit_my_external_account", "get_unread", "delete_unread", "get_clip_folder", "create_clip_folder", "edit_clip_folder", "delete_clip_folder", ]  # noqa: E501

        Keyword Args:
            value (str): ??????????????????., must be one of ["get_webhook", "create_webhook", "edit_webhook", "delete_webhook", "access_others_webhook", "get_bot", "create_bot", "edit_bot", "delete_bot", "access_others_bot", "bot_action_join_channel", "bot_action_leave_channel", "create_channel", "get_channel", "edit_channel", "delete_channel", "change_parent_channel", "edit_channel_topic", "get_channel_star", "edit_channel_star", "get_my_tokens", "revoke_my_token", "get_clients", "create_client", "edit_my_client", "delete_my_client", "manage_others_client", "upload_file", "download_file", "delete_file", "get_message", "post_message", "edit_message", "delete_message", "report_message", "get_message_reports", "create_message_pin", "delete_message_pin", "get_channel_subscription", "edit_channel_subscription", "connect_notification_stream", "register_fcm_device", "get_stamp", "create_stamp", "edit_stamp", "edit_stamp_created_by_others", "delete_stamp", "add_message_stamp", "remove_message_stamp", "get_my_stamp_history", "get_stamp_palette", "create_stamp_palette", "edit_stamp_palette", "delete_stamp_palette", "get_user", "register_user", "get_me", "edit_me", "change_my_icon", "change_my_password", "edit_other_users", "get_user_qr_code", "get_user_tag", "edit_user_tag", "get_user_group", "create_user_group", "create_special_user_group", "edit_user_group", "delete_user_group", "edit_others_user_group", "web_rtc", "get_my_sessions", "delete_my_sessions", "get_my_external_account", "edit_my_external_account", "get_unread", "delete_unread", "get_clip_folder", "create_clip_folder", "edit_clip_folder", "delete_clip_folder", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """UserPermission - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): ??????????????????., must be one of ["get_webhook", "create_webhook", "edit_webhook", "delete_webhook", "access_others_webhook", "get_bot", "create_bot", "edit_bot", "delete_bot", "access_others_bot", "bot_action_join_channel", "bot_action_leave_channel", "create_channel", "get_channel", "edit_channel", "delete_channel", "change_parent_channel", "edit_channel_topic", "get_channel_star", "edit_channel_star", "get_my_tokens", "revoke_my_token", "get_clients", "create_client", "edit_my_client", "delete_my_client", "manage_others_client", "upload_file", "download_file", "delete_file", "get_message", "post_message", "edit_message", "delete_message", "report_message", "get_message_reports", "create_message_pin", "delete_message_pin", "get_channel_subscription", "edit_channel_subscription", "connect_notification_stream", "register_fcm_device", "get_stamp", "create_stamp", "edit_stamp", "edit_stamp_created_by_others", "delete_stamp", "add_message_stamp", "remove_message_stamp", "get_my_stamp_history", "get_stamp_palette", "create_stamp_palette", "edit_stamp_palette", "delete_stamp_palette", "get_user", "register_user", "get_me", "edit_me", "change_my_icon", "change_my_password", "edit_other_users", "get_user_qr_code", "get_user_tag", "edit_user_tag", "get_user_group", "create_user_group", "create_special_user_group", "edit_user_group", "delete_user_group", "edit_others_user_group", "web_rtc", "get_my_sessions", "delete_my_sessions", "get_my_external_account", "edit_my_external_account", "get_unread", "delete_unread", "get_clip_folder", "create_clip_folder", "edit_clip_folder", "delete_clip_folder", ]  # noqa: E501

        Keyword Args:
            value (str): ??????????????????., must be one of ["get_webhook", "create_webhook", "edit_webhook", "delete_webhook", "access_others_webhook", "get_bot", "create_bot", "edit_bot", "delete_bot", "access_others_bot", "bot_action_join_channel", "bot_action_leave_channel", "create_channel", "get_channel", "edit_channel", "delete_channel", "change_parent_channel", "edit_channel_topic", "get_channel_star", "edit_channel_star", "get_my_tokens", "revoke_my_token", "get_clients", "create_client", "edit_my_client", "delete_my_client", "manage_others_client", "upload_file", "download_file", "delete_file", "get_message", "post_message", "edit_message", "delete_message", "report_message", "get_message_reports", "create_message_pin", "delete_message_pin", "get_channel_subscription", "edit_channel_subscription", "connect_notification_stream", "register_fcm_device", "get_stamp", "create_stamp", "edit_stamp", "edit_stamp_created_by_others", "delete_stamp", "add_message_stamp", "remove_message_stamp", "get_my_stamp_history", "get_stamp_palette", "create_stamp_palette", "edit_stamp_palette", "delete_stamp_palette", "get_user", "register_user", "get_me", "edit_me", "change_my_icon", "change_my_password", "edit_other_users", "get_user_qr_code", "get_user_tag", "edit_user_tag", "get_user_group", "create_user_group", "create_special_user_group", "edit_user_group", "delete_user_group", "edit_others_user_group", "web_rtc", "get_my_sessions", "delete_my_sessions", "get_my_external_account", "edit_my_external_account", "get_unread", "delete_unread", "get_clip_folder", "create_clip_folder", "edit_clip_folder", "delete_clip_folder", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
