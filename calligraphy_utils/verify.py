import yaml
import os

required_file_paths = [
    './site.yml'
]

required_dir_paths = [
    './posts',
    './posts/published'
    './themes'
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def console_error(text):
    print(bcolors.WARNING + str(text) + bcolors.ENDC)

def verify(log=True):
    for path in required_file_paths:
        if os.path.isfile('.'+path):
            if log:
                console_error('File "%s" required. View https://github.com/terrillo/calligraphy-cms' % (path))

    for path in required_dir_paths:
        os.path.isdir('.'+path)

    return True

verify()
