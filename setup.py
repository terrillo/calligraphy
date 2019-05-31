from setuptools import setup

setup(
    name='calligraphy',
    version='0.1',
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
