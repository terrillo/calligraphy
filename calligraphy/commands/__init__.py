import os
import sys
from jinja2 import Template
import yaml

from flask import Flask
StaticServer = Flask(__name__, root_path='html')
StaticServer.jinja_env.cache = {}
StaticServer.jinja_env.auto_reload = True
StaticServer.config['TEMPLATES_AUTO_RELOAD'] = True

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
                    parse = yaml.load(open('./posts/published/'+path, 'r'), Loader=yaml.FullLoader)
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

    def export(self, yell=True):
        if self.verify():
            os.system("rm -rf ./html")
            os.system("mkdir ./html")
            os.system("mkdir ./html/posts")
            self.config['posts'] = []

            header = Template(open('./themes/%s/_header.html' % (self.config['theme'])).read()).render(self.config)
            footer = Template(open('./themes/%s/_footer.html' % (self.config['theme'])).read()).render(self.config)

            map = {
                'index': {
                    'template': Template(open('./themes/%s/index.html' % (self.config['theme'])).read()),
                    'data': self.config,
                }
            }
            pages = map.keys()
            for path in os.listdir('./posts/published'):
                if '.yml' in path and not path == '_template.yml':
                    post = yaml.load(open('./posts/published/'+path, 'r'), Loader=yaml.FullLoader)
                    post['body'] = '<p></p>'.join(post['body'].split('\n'))

                    # Single page
                    post_template = Template(open('./themes/%s/single.html' % (self.config['theme'])).read())
                    slug = path.replace(' ', '-').replace(' ', '--').replace('.yml', '')
                    file = open("./html/posts/%s.html" % (slug),"w")
                    file.write(header + post_template.render(post) + footer)

                    # Homepage
                    post['slug'] = slug
                    map['index']['data']['posts'].append(post)

            for page in pages:
                file = open("./html/%s.html" % (page),"w")
                file.write(header + map[page]['template'].render(map[page]['data']) + footer)
            if yell:
                console_success("Export: success")
        else:
            if yell:
                console_error("Export: failed")

        return True

    def run(self):
        raise NotImplementedError('Internal error https://github.com/terrillo/calligraphy/issues')

from .export import *
from .verify import *
from .static import *
