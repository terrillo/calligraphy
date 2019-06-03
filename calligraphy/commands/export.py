"""The export command."""

from json import dumps

from . import Calligraphy

class Export(Calligraphy):
    """Say hello, world!"""

    def run(self):
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        print('>>>>>')
        Calligraphy.export(self)
        print('>>>>>')
