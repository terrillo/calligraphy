from setuptools import setup

setup(
    name='calligraphy',
    version='0.1.0',
    author="Terrillo Walls",
    author_email="terrillo@terrillo.com",
    url="https://github.com/terrillo/calligraphy",
    description="A static blog generator.",
    long_description=open("README.md").read(),
    py_modules=['calligraphy'],
    install_requires=[
        'pyyaml',
        'jinja2'
    ],
    python_requires=">=3.0.*",
    entry_points='''
        [console_scripts]
        calligraphy=calligraphy:cli
        calligraphy static=calligraphy:cli
    ''',
)
