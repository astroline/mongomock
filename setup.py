from pathlib import Path

from setuptools import find_packages
from setuptools import setup


README_PATH = Path(__file__).with_name('README.rst')


setup(
    name='mongomock',
    use_scm_version={'fallback_version': '4.3.0'},
    setup_requires=['setuptools-scm==6.4.2'],
    description='Fake pymongo stub for testing simple MongoDB-dependent code',
    long_description=README_PATH.read_text(encoding='utf-8'),
    long_description_content_type='text/x-rst',
    license='ISC',
    author='Rotem Yaari, Martin Domke, Pascal Corpet',
    url='https://github.com/mongomock/mongomock',
    project_urls={
        'Changelog': 'https://github.com/mongomock/mongomock/blob/develop/CHANGELOG.md',
    },
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    package_data={'mongomock': ['py.typed', '*.pyi']},
    python_requires='>=3.6',
    install_requires=[
        "importlib-metadata==4.8.3; python_version < '3.8'",
        "packaging<22; python_version < '3.7'",
        "packaging; python_version >= '3.7'",
        'pytz',
        "sentinels<1.1; python_version < '3.9'",
        "sentinels; python_version >= '3.9'",
    ],
    extras_require={
        'pyexecjs': ['pyexecjs'],
        'pymongo': [
            "pymongo<4.2; python_version < '3.7'",
            "pymongo; python_version >= '3.7'",
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database',
    ],
)
