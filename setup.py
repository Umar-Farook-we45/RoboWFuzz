from setuptools import setup

setup(
    name='RoboWFuzz',
    version='0.1',
    packages=[''],
    package_dir={'': 'robowfuzz'},
    url='',
    license='AGPL',
    author='Abhay Bhargav',
    author_email='abhay@we45.com',
    install_requires = ['wfuzz','robotframework'],
    description='Currently a Directory Bruter built on the wfuzz library'
)
