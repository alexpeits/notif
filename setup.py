from distutils.cmd import Command
from setuptools import setup, find_packages


class UserInitCommand(Command):

    description = 'create database for user that installs'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from notif.db.utils import create_tables
        create_tables()


setup(
    name='notif',
    version=0.1,
    author='Alex Peitsinis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'new-todo = notif.bin.new_todo:new_todo',
            'check-todo = notif.bin.check_todo:check_todo',
        ]
    },
    install_requires=[
        'SQLAlchemy',
        'SQLAlchemy_utils',
        'arrow',
    ],
    include_package_data=True,
    cmdclass={
        'user_init': UserInitCommand
    },
    zip_safe=False
)
