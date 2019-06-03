import os
import sys
import yaml

from ..utils import *

class Calligraphy(object):
    """A Calligraphy master class."""

    def __init__(self, options, *args, **kwargs):
        self.required_file_paths = [
            './site.yml'
        ]

        self.required_dir_paths = [
            './posts',
            './posts/published',
            './themes'
        ]
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def verify_site_config(self, log):
        required_fields = [
            'site_name',
            'theme'
        ]
        for field in required_fields:
            if field not in self.config:
                if log:
                    console_error('site.yml missing "%s"' % field)
                return False
        if not os.path.isdir('./themes/%s' % (self.config['theme'])):
            if log:
                console_error('"%s" theme not found' % (self.config['theme']))
        return True

    def verify_each_post(self, log):
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
                    parse = yaml.load(open('./posts/published/'+path, 'r'))
                except:
                    if log:
                        console_error('Blog post: "%s" is an invalid yaml file.' % (path))
                    return False

                for field in required_fields:
                    if field not in parse:
                        if log:
                            console_warn('"%s" missing a "%s"' % (path, field))

        return True


    def verify(self, log=True):
        # Required files
        for path in self.required_file_paths:
            if os.path.isfile(path):
                try:
                    parse = yaml.load(open(path, 'r'), Loader=yaml.BaseLoader)
                    self.config = parse
                except:
                    if log:
                        console_error('"%s" is an invalid yaml file.' % (path))
                    return False
            else:
                if log:
                    console_error('Required file "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
                return False

        # Config Verify
        config_verify = self.verify_site_config(log)
        if not config_verify:
            return False

        # Required Directories
        for path in self.required_dir_paths:
            if not os.path.isdir(path):
                if log:
                    console_error('Required directory "%s" not found. View https://github.com/terrillo/calligraphy-cms' % (path))
                return False

        # Verify each post
        post_veify = self.verify_each_post(log)
        if not post_veify:
            return False

        return True

    def export(self):
        if self.verify():
            console_success("Export: success")
        else:
            console_error("Export: failed")


        return True

    def run(self):
        raise NotImplementedError('Internal error https://github.com/terrillo/calligraphy/issues')

from .export import *
from .verify import *
