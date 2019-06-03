"""The export command."""

from json import dumps

from . import Calligraphy

class Export(Calligraphy):
    """Say hello, world!"""

    def run(self):
        Calligraphy.export(self)
