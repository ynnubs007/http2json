#encoding: utf-8
import io

from http2json import __version__
from setuptools import find_packages, setup

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='http2json',
    version=__version__,
    description='http2json',
    long_description=long_description,
    author='ynnubs7',
    author_email='smart@126.com',
    url='https://github.com/ynnubs007/http2json',
    license='MIT',
    packages=find_packages(exclude=['test.*', 'test']),
    package_data={},
    keywords='har converter json',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'http2json=http2json.cli:main'
        ]
    }
)