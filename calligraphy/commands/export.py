"""The export command."""

from json import dumps

from .base import Base

class Export(Base):
    """Say hello, world!"""

    def run(self):
        print('Hello, world!')
