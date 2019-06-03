"""The static command."""

import os
import json

from . import Calligraphy
from . import StaticServer

class Static(Calligraphy):
    """Say hello, world!"""

    def run(self):
        if Calligraphy.verify(self):
            Calligraphy.export(self, False)

            # Index
            @StaticServer.route('/', methods=['GET'])
            def index():
                return open('./html/index.html').read()

            # Posts
            @StaticServer.route('/posts/<page>', methods=['GET'])
            def posts(page):
                if os.path.isfile('./html/posts/%s' % page):
                    return open('./html/posts/%s' % page).read()
                else:
                    return 'POST NOT FOUND'

            StaticServer.run(host='0.0.0.0', port=int(self.options['--port']))
