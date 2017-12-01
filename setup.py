import sys
from distutils.core import setup
from setuptools import find_packages

if sys.version_info < 3:
    sys.exit('Sorry, Python < 3 is not supported')

setup(
    name='scraping_python',
    version='0.0.1',
    url='https://github.com/panage/scraper-python',
    license='',
    author='fu-taku',
    author_email='',
    description='Study scraping python',
    install_requires=['requests', 'beautifulsoup4']
)
