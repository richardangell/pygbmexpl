import setuptools
import re



def get_version():
    '''Function to read package version number from file.'''

    VERSION_FILE='pygbmexpl/_version.py'
    version_str = open(VERSION_FILE, 'rt').read()
    VERSION_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VERSION_RE, version_str, re.M)
    if mo:
        version = mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in %s.' % (VERSION_FILE,))

    return version


def read_long_description():
    '''Function to read long description from README.'''

    with open("README.md", "r") as fh:

        long_description = fh.read()

    return long_description


# with open('requirements.txt') as f:
#     required = f.read().splitlines()


setuptools.setup(
    name="pygbmexpl",
    version=get_version(),
    author="Richard Angell",
    author_email="richardangell37@gmail.com",
    description="Package to explain gbm predictions",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/richardangell/pygbmexpl",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas>=0.24",
        "xgboost>=0.81"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

