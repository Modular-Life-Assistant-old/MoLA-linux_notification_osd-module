import os

from core import settings
from helpers.modules.NotificationModule import NotificationModule


class Module(NotificationModule):
    def is_available(self):
        return os.system('notify-send --help > /dev/null') == 0

    def send(self, msg, image=None, sound=None):
        os.system('notify-send "%s" "%s" &' % (settings.NAME, msg))