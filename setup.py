from setuptools import setup

APP = ['monitor2app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['psutil'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
