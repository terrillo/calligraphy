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

def console_warn(text):
    print(bcolors.WARNING + str(text) + bcolors.ENDC)

def verify_site_config(log):
    required_fields = [
        'site_name',
        'theme'
    ]
    site_file = yaml.load(open('./site.yml', 'r'), Loader=yaml.FullLoader)
    for field in required_fields:
        if field not in site_file:
            if log:
                console_error('site.yml missing "%s"' % field)
            return False
    if not os.path.isdir('./themes/%s' % (site_file['theme'])):
        if log:
            console_error('"%s" theme not found' % (site_file['theme']))
    return True

def verify_each_post(log):
    required_fields = [
        'title',
        'date',
        'author',
        'summary',
        'body'
    ]
    for path in os.listdir('./posts/published'):
        if '.yml' in path:
            try:
                parse = yaml.load(open('./posts/published/'+path, 'r'), Loader=yaml.FullLoader)
            except:
                if log:
                    console_error('"%s" is an invalid yaml file.' % (path))
                return False

            for field in required_fields:
                if field not in parse:
                    if log:
                        console_warn('"%s" missing a "%s"' % (path, field))

    return True


def verify(log=True):

    # Required files
    for path in required_file_paths:
        if os.path.isfile(path):
            try:
                parse = yaml.load(open(path, 'r'), Loader=yaml.BaseLoader)
            except:
                if log:
                    console_error('"%s" is an invalid yaml file.' % (path))
                return False
        else:
            if log:
                console_error('Required file "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
            return False

    # Config Verify
    config_verify = verify_site_config(log)
    if not config_verify:
        return False

    # Required Directories
    for path in required_dir_paths:
        if not os.path.isdir(path):
            if log:
                console_error('Required directory "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
            return False

    # Verify each post
    post_veify = verify_each_post(log)
    if not post_veify:
        return False

    return True
