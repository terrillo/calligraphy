"""The export command."""

from json import dumps

from . import Calligraphy

class Verify(Calligraphy):
    """Say hello, world!"""

    def run(self):
        Calligraphy.verify(self)
