import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='calligraphy',
        version='0.7.0',
        author="Terrillo Walls",
        author_email="terrillo@terrillo.com",
        url="https://github.com/terrillo/calligraphy",
        description="A static blog generator.",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        install_requires=[
            'pyyaml',
            'Jinja2>=2.10.1'
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
            'console_scripts': ['calligraphy=calligraphy:cli'],
        }
    )
