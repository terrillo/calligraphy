"""
calligraphy
Usage:
  calligraphy export
  calligraphy -h | --help
  calligraphy --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  calligraphy export
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    import calligraphy.commands
    options = docopt(__doc__, version=VERSION)

    # Dynamically match the command
    for (k, v) in options.items():
        if hasattr(calligraphy.commands, k) and v:
            module = getattr(calligraphy.commands, k)
            calligraphy.commands = getmembers(module, isclass)
            command = [command[1] for command in calligraphy.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
