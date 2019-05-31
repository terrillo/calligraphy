import os
from jinja2 import Template

from verify import *

verified = verify(False)
if verified:
    if not os.path.isdir('./dist'):
        os.system("mkdir ./dist")
    if not os.path.isdir('./dist/posts'):
        os.system("mkdir ./dist/posts")
    site_file = yaml.load(open('./site.yml', 'r'), Loader=yaml.FullLoader)
    site_file['posts'] = []

    header = Template(open('./themes/%s/_header.html' % (site_file['theme'])).read()).render(site_file)
    footer = Template(open('./themes/%s/_footer.html' % (site_file['theme'])).read()).render(site_file)

    map = {
        'index': {
            'template': Template(open('./themes/%s/index.html' % (site_file['theme'])).read()),
            'data': site_file,
        }
    }
    pages = map.keys()
    for path in os.listdir('./posts/published'):
        if '.yml' in path:
            post = yaml.load(open('./posts/published/'+path, 'r'), Loader=yaml.FullLoader)
            post['body'] = '<p></p>'.join(post['body'].split('\n'))

            # Single page
            post_template = Template(open('./themes/%s/single.html' % (site_file['theme'])).read())
            slug = path.replace(' ', '-').replace(' ', '--').replace('.yml', '')
            file = open("./dist/posts/%s.html" % (slug),"w")
            file.write(header + post_template.render(post) + footer)

            # Homepage
            post['slug'] = slug
            map['index']['data']['posts'].append(post)

    for page in pages:
        file = open("./dist/%s.html" % (page),"w")
        file.write(header + map[page]['template'].render(map[page]['data']) + footer)
else:
    print(verified)
