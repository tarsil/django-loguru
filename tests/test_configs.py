from django.conf import settings as configs
from django.test import override_settings

from django_loguru.configs import DEFAULTS, Configs


@override_settings(DJANGO_LOGURU_MIDDLEWARE={})
def test_check_configs_if_user_didnt_setconfigs():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'MESSAGE_FORMAT': '{message}'})
def test_check_configs_if_user_set_default_format_true_and_set_message_format():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': False, 'MESSAGE_FORMAT': '{message}'})
def test_check_configs_if_user_set_default_format_false_and_set_message_format():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == False
    assert settings.MESSAGE_FORMAT == '{message}'
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': False})
def test_check_configs_if_user_set_default_format_false_but_didnt_set_message_format():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == False
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True})
def test_check_configs_if_user_set_default_format_true_and_didnt_set_message_format():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'MESSAGE_FORMAT': '{message}'})
def test_check_configs_if_user_didnt_set_default_format_but_set_message_format():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': ''})
def test_check_configs_if_user_set_wrong_data():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'LOG_POST': True})
def test_check_configs_if_user_set_log_post_to_true():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == True
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'LOG_PUT': True})
def test_check_configs_if_user_set_log_put_to_true():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == True
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'LOG_PATCH': True})
def test_check_configs_if_user_set_log_patch_to_true():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == True
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'LOG_DELETE': True})
def test_check_configs_if_user_set_log_delete_to_true():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == True
    assert settings.LOG_USER == DEFAULTS['LOG_USER']


@override_settings(DJANGO_LOGURU_MIDDLEWARE={'DEFAULT_FORMAT': True, 'LOG_USER': False})
def test_check_configs_if_user_set_log_user_to_false():
    settings = Configs(configs)
    assert settings.DEFAULT_FORMAT == DEFAULTS['DEFAULT_FORMAT']
    assert settings.MESSAGE_FORMAT == DEFAULTS['MESSAGE_FORMAT']
    assert settings.LOG_POST == DEFAULTS['LOG_POST']
    assert settings.LOG_PUT == DEFAULTS['LOG_PUT']
    assert settings.LOG_PATCH == DEFAULTS['LOG_PATCH']
    assert settings.LOG_DELETE == DEFAULTS['LOG_DELETE']
    assert settings.LOG_USER == False