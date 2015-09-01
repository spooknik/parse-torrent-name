import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    description = f.read()

setup(
    name='parse-torrent-name',
    version=__import__('ptn').__version__,
    author=__import__('ptn').__author__,
    author_email=__import__('ptn').__email__,
    license=__import__('ptn').__license__,
    url='https://github.com/divijbindlish/parse-torrent-name',
    description='Parse torrent name of a movie or TV show',
    long_description=description,
    packages=['PTN'],
    keywords=('parse parser torrent torrents name names proper rename '
              'movie movies tv show shows series extract find quality '
              'group codec audio resolution title season episode year ')
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Text Processing'
    ]

)
