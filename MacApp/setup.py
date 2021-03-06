"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['PSDownloaderGUI.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

import ez_setup
ez_setup.use_setuptools()

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
