"""
Molokai CMS
"""
from flask import Flask


class MolokaiCMS(object):
    """
    Base class to initialize Molokai CMS

    Arguments:
        project_dir (str): Full path to main application
        project_name (str): Name of application

    Example:
    in /path/to/main/application/app.py

        from molokai_cms import MolokaiCMS

        molokai = MolokaiCMS('/path/to/main/application/', 'My Internet Page')
        // Register Views for my application
        molokai.register_views()

        if __name__ == '__main__':
            molokai.app.run()

    Then in terminal:

        $ python /path/to/main/application/app.py

             * Running on http://127.0.0.1:5000/
    """

    def __init__(self, project_dir, project_name):
        self.project_dir = project_dir
        self.project_name = project_name
        self.app = Flask(self.project_name)

    def register_views(self, apps=None):
        """
        Register views for this application

        Arguments:
            apps (list or tuple): List (tuple) of third-party application's views or None
        """