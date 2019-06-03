"""The export command."""

from json import dumps

from ..utils import *
from . import Calligraphy

class Verify(Calligraphy):
    """Say hello, world!"""

    def run(self):
        if Calligraphy.verify(self):
            console_success("Verification: success")
