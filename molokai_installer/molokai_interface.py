# -*- coding: utf-8 -*-

__author__ = "Nikolay Dolganov"
__email__ = "SirNikolasd@yandex.ru"


"""
This script contains interface for the projects administration.
Interface is used for the creation, administration, repairing of the projects.
Interface can be used from GUI interface or from the console with existing scripts.
"""


class Project(object):
    """
    This interface is needed to administrate project from the existing directory.

    :argument project_dir: str Full path of the project
    """

    def __init__(self, project_dir):
        self.project_dir = project_dir

    def __read_settings(self):
        """
        Try to read settings file of the project
        :return: bool Result of the settings read - True or False
        """

    def create_project(self):
        """
        Creates new project
        :return: dict Result of the project creation - dictionary with information
        """

    def check_project(self):
        """
        Check project settings and scripts to availability
        :return: dict Result of the checking
        """

    def repair_project(self):
        """
        Repairs project files with saves of the existing files
        :return: dict Result of the repairing
        """

    def recreate_project(self):
        """
        Deletes old project and creates new with same name and in the same dir
        :return: dict Result of the recreation
        """
