"""
Molokai CMS

See on GitHub: https://github.com/werevolff/molokai

"""
from distutils.core import setup
import os

BASE_DIR = os.path.dirname(__file__)

REQUIREMENTS = []

with open(os.path.join(BASE_DIR, 'requirements.txt')) as f:
    for line in f.readlines():
        REQUIREMENTS.append(line)

setup(
    name='Molokai CMS',
    version='0.1.dev',
    packages=['molokai_fs', 'molokai_auth', 'molokai_themes', 'molokai_admin', 'molokai_cms', 'molokai_mailing'],
    url='http://www.molokai-cms.org/',
    license='GNU GPL v.2',
    author='Nikolay Werevolff Dolganov',
    author_email='sirnikolasd@yandex.ru',
    description='Flask-based CMS',
    install_requires=REQUIREMENTS
)
