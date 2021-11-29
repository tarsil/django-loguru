DEFAULTS = {
    'DEFAULT_FORMAT': True,
    'MESSAGE_FORMAT': "<b><green>{time}</green> <blue>{message}</blue></b>",
    'LOG_POST': False,
    'LOG_PUT': False,
    'LOG_PATCH': False,
    'LOG_DELETE': False,
    'LOG_USER': True
}

class Configs:
    def __init__(self, settings):
        self.configs = getattr(settings, 'DJANGO_LOGURU_MIDDLEWARE', DEFAULTS)
        self.set_configs()

        self.DEFAULT_FORMAT = self.configs['DEFAULT_FORMAT']
        self.MESSAGE_FORMAT = self.configs['MESSAGE_FORMAT']
        self.LOG_POST = self.configs['LOG_POST']
        self.LOG_PUT = self.configs['LOG_PUT']
        self.LOG_PATCH = self.configs['LOG_PATCH']
        self.LOG_DELETE = self.configs['LOG_DELETE']
        self.LOG_USER = self.configs['LOG_USER']

    def set_configs(self):
        """
        Sets and validates the configurations.
        """
        if self.configs == {}:
            self.configs = DEFAULTS
            return

        default_keys = {k:v for k,v in DEFAULTS.items() if k not in self.configs.keys()}
        self.configs.update(default_keys)

        if 'DEFAULT_FORMAT' not in list(self.configs.keys()):
            self.configs['DEFAULT_FORMAT'] = DEFAULTS['DEFAULT_FORMAT']
            self.configs['MESSAGE_FORMAT'] = DEFAULTS['MESSAGE_FORMAT']
        elif not isinstance(self.configs['DEFAULT_FORMAT'], bool):
            self.configs['DEFAULT_FORMAT'] = DEFAULTS['DEFAULT_FORMAT']
            self.configs['MESSAGE_FORMAT'] = DEFAULTS['MESSAGE_FORMAT']
        elif 'DEFAULT_FORMAT' in list(self.configs.keys()):
            if not self.configs['DEFAULT_FORMAT'] and 'MESSAGE_FORMAT' in list(self.configs.keys()):
                self.configs['DEFAULT_FORMAT'] = self.configs['DEFAULT_FORMAT']
                self.configs['MESSAGE_FORMAT'] = self.configs['MESSAGE_FORMAT']
            elif self.configs['DEFAULT_FORMAT'] and 'MESSAGE_FORMAT' not in list(self.configs.keys()):
                self.configs['DEFAULT_FORMAT'] = self.configs['DEFAULT_FORMAT']
                self.configs['MESSAGE_FORMAT'] = DEFAULTS['MESSAGE_FORMAT']
            else:
                self.configs['DEFAULT_FORMAT'] = self.configs['DEFAULT_FORMAT']
                self.configs['MESSAGE_FORMAT'] = DEFAULTS['MESSAGE_FORMAT']
        else:
            self.configs['DEFAULT_FORMAT'] = self.configs['DEFAULT_FORMAT']
            self.configs['MESSAGE_FORMAT'] = self.configs['MESSAGE_FORMAT']