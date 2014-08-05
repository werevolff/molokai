"""
Molokai CMS
"""
from flask import Flask
import os

BASE_DIR = os.path.dirname(__file__)

molokai = Flask('molokai_cms')

@molokai.route('/')
def hello_world():
    return molokai.auto_find_instance_path()