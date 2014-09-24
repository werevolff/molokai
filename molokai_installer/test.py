# -*- coding: utf-8 -*-

__author__ = "Nikolay Dolganov"
__email__ = "SirNikolasd@yandex.ru"

"""
Test MolokaiCMS installer
"""

import nose
from flask.ext.testing import TestCase
import os
from shutil import rmtree
from flask.ext.babel import lazy_gettext as _
from flask import Flask
from flask.ext.babel import Babel


# Current file directory. It used for calculating default test dir
# But in production it can be not work, because of permissions
CURRENT_DIR = os.path.curdir


class DirectoryAlreadyExists(Exception):
    """
    Exception: Test Directory Already Exists
    """
    pass


class TestInstallerInterface(TestCase):
    """
    Test molokai_interface: functions for the project administration
    """

    def create_app(self):
        """
        We must to create application at first
        """
        app = Flask(__name__)
        babel = Babel(app)
        return app

    def setUp(self):
        # Default directory for test project
        self.test_directory = os.path.join(CURRENT_DIR, 'test_project')
        self.__create_directory()

    def __create_directory(self):
        """
        Try to create test_project directory
        """
        try:
            if not os.path.exists(self.test_directory):
                os.makedirs(self.test_directory)
            else:
                raise DirectoryAlreadyExists(_('Directory {0} already exists.').format(self.test_directory))
        except OSError:
            # If errors, we cannot to create this dir. Tests covers this troubles
            pass

    def test_directory_exists(self):
        """
        Tests, that test directory exists
        """
        self.assertTrue(os.path.exists(self.test_directory),
                        msg=_('Directory "{0}" does not exists').format(self.test_directory))

    def test_if_is_directory(self):
        """
        Test if test_directory is folder, not file
        """
        self.assertTrue(os.path.isdir(self.test_directory),
                        msg=_('"{0}" - is not a directory').format(self.test_directory))

    def test_directory_permissions(self):
        """
        Test Permissions to write into test directory
        """
        self.assertTrue(os.access(self.test_directory, os.W_OK),
                        msg=_('Sorry, but directory "{0}" is not permitted to write').format(self.test_directory))

    def tearDown(self):
        if os.path.exists(self.test_directory):
            try:
                rmtree(self.test_directory)
            except OSError:
                pass

if __name__ == '__main__':
    nose.main()