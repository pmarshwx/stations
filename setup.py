import distutils.sysconfig
from distutils.core import setup
from distutils.command.install_data import install_data
import os, sys


# Setup Variables
dirname = 'stations'
packages = ['stations']
package_dir = {'stations': 'stations'}
package_data = {'stations': ['data/*.txt']}
desc = 'Python Module for Retrieving Lon, Lat, and Priority of METR Stations'
setup_path = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(setup_path, dirname))
module_path = distutils.sysconfig.get_python_lib()
include_files = ['README']
data_files = [(os.path.join(module_path, dirname), include_files)]


import version
version.write_git_version()
ver = version.get_version()
sys.path.pop()

setup(
    name                    = 'stations',
    version                 = ver,
    description             = desc,
    author                  = 'Patrick Marsh',
    author_email            = 'patrick.marsh@noaa.gov',
    url                     = '',
    download_url            = '',
    packages                = packages,
    package_dir             = package_dir,
    package_data            = package_data,
    data_files              = data_files,
    scripts                 = [],
)
