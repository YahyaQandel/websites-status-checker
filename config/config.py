import sys


class Configuration(object):
    def get_configuration(self):
        if "nosetests" in sys.argv[0]:
            from base import settings
            settings = settings
            from test import settings as test_settings
            settings.update(test_settings)
        else:
            from base import settings
            settings = settings
        return settings
