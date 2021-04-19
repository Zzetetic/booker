
from setuptools import setup, find_packages
from booker.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='booker',
    version=VERSION,
    description='Application for calculating book pages for printing',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='John Doe',
    author_email='john.doe@example.com',
    url='https://github.com/Zzetetic/booker/',
    license='gpl3',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'booker': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        booker = booker.main:main
    """,
)
