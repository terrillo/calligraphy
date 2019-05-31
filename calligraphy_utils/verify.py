import yaml
import os
import sys

required_file_paths = [
    './site.yml'
]

required_dir_paths = [
    './posts',
    './posts/published',
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
    print(bcolors.FAIL + str(text) + bcolors.ENDC)

def verify_site_config():
    required_fields = [
        'site_name',
        'theme'
    ]
    site_file = yaml.load(open('./site.yml', 'r'), Loader=yaml.FullLoader)
    for field in required_fields:
        if field not in site_file:
            console_error('site.yml missing "%s"' % field)
            return False

    return True


def verify(log=True):
    for path in required_file_paths:
        if os.path.isfile(path):
            try:
                parse = yaml.load(open(path, 'r'), Loader=yaml.FullLoader)
            except:
                console_error('"%s" is an invalid yaml file.' % (path))
                return False
        else:
            if log:
                console_error('Required file "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
            return False

    config_verify = verify_site_config()
    if not config_verify:
        return False

    for path in required_dir_paths:
        if not os.path.isdir(path):
            if log:
                console_error('Required directory "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
            return False

    return True

verify()
