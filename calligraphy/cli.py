"""
calligraphy
Usage:
  calligraphy verify
  calligraphy export
  calligraphy static
  calligraphy static --port=<number>
  calligraphy -h | --help
  calligraphy --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
  --port=<number>                   HTTP port [default: 8080].
Examples:
  calligraphy export
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/terrillo/calligraphy
"""

import os
import sys

from inspect import getmembers, isclass
from docopt import docopt

from . import __version__ as VERSION
from .utils import *

def main():
    """Main CLI entrypoint."""
    import calligraphy.commands
    options = docopt(__doc__, version=VERSION)

    # Look for project
    if not os.path.isfile('./site.yml'):
        console_error('Not a "Calligraphy" project!')
        sys.exit()

    # Dynamically match the command
    for (k, v) in options.items():
        if hasattr(calligraphy.commands, k) and v:
            module = getattr(calligraphy.commands, k)
            calligraphy.commands = getmembers(module, isclass)
            command = [command[1] for command in calligraphy.commands if command[0] != 'Calligraphy'][0]
            command = command(options)
            command.run()
