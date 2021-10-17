try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple PySide6 project structure.',
    'author': 'Some One',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'someone@email.com',
    'version': '0.1',
    'install_requires': ['PySide6', 'PyInstaller'],
    'packages': [],
    'scripts': [],
    'name': 'pyside6_example_project'
}

setup(**config)

