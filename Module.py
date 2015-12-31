import os

from core import settings
from helpers.modules.BaseModule import BaseModule


class Module(BaseModule):
    def is_available(self):
        return os.system('notify-send --help > /dev/null') == 0

    def send(self, event):
        """Receive notification."""
        msg = event.kwargs.get('msg', None)

        if msg:
            os.system('notify-send "%s" "%s" &' % (settings.NAME, msg))