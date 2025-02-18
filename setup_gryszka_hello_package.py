import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.3'
PACKAGE_NAME = 'gryszka_hello_package'
AUTHOR = 'Gryszka'
AUTHOR_EMAIL = 'romanowicz.g@gmail.com'
URL = 'https://github.com/Gryszka/public_nested_packages/src/gryszka_hello_package'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Testing WHL purpose. Hello World'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ['gryszka_another_package']
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
]
KEYWORDS = 'testing example package'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)