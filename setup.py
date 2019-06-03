import setuptools
from calligraphy import __version__ as VERSION

if __name__ == "__main__":
    setuptools.setup(
        name='calligraphy',
        version=VERSION,
        author="Terrillo Walls",
        author_email="terrillo@terrillo.com",
        url="https://github.com/terrillo/calligraphy",
        description="A static blog generator.",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        install_requires=[
            'PyYAML>=3.10',
            'Jinja2>=2.10.1',
            'docopt==0.6.2',
            'Flask==1.0.3'
        ],
        project_urls={
            "Bug Tracker": "https://github.com/terrillo/calligraphy/issues",
            "Documentation": "https://github.com/terrillo/calligraphy",
            "Source Code": "https://github.com/terrillo/calligraphy",
        },
        python_requires=">=3.0.*",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        entry_points = {
            'console_scripts': [
                'calligraphy=calligraphy.cli:main'
            ],
        }
    )
