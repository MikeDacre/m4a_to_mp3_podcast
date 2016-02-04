"""
Setup script for m4a_to_mp3_podcast
Last modified: 2016-02-04 13:31
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
from os import listdir

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Generate a list of python scripts
scpts = []
for i in listdir(here + '/bin'):
    scpts.append('bin/' + i)

setup(
    name='podcast_convert',
    version='0.1',
    description=('Convert an m4a podcast to mp3 maintaining feed structure, ' +
                 'works with podcast apps'),
    long_description=long_description,
    url='https://github.com/MikeDacre/m4a_to_mp3_podcast',
    author='Michael Dacre',
    author_email='mike.dacre@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='podcast, m4a, mp3, rss, convert',

    #  install_requires=[],
    packages=['podcast_convert'],
    scripts=scpts
)
