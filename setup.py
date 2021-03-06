# $Id: setup.py 4232 2012-08-20 06:01:41Z ming $
#
# pjsua Setup script.
#
# Copyright (C) 2003-2008 Benny Prijono <benny@prijono.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA 
#
from setuptools import setup, Extension, find_packages

import pkgconfig
import versioneer

def modversion_backport(package):
    return pkgconfig.pkgconfig._query(package, '--modversion')

if hasattr(pkgconfig, 'modversion'):
    modversion = pkgconfig.modversion
else:
    modversion = modversion_backport

package = 'libpjproject'

pj_version = modversion(package)

# This removes a needless dependency on libavdevice.
def filter_libs(lib):
	return lib not in ('avdevice',)

d = pkgconfig.parse(package)
pj_inc_dirs = d['include_dirs']
pj_lib_dirs = d['library_dirs']
pj_libs = list(filter(filter_libs, d['libraries']))
pj_defs = d['define_macros']
extra_link_args = d['extra_link_args']

setup(name="pjsua", 
      version=versioneer.get_version(),
      description='SIP User Agent Library based on PJSIP (%s)' % pj_version,
      url='https://github.com/avian2/python3-pjsip',
      packages=find_packages(),
      ext_modules = [Extension("pjsua._pjsua",
                               ["_pjsua.c"], 
                               define_macros=pj_defs,
                               include_dirs=pj_inc_dirs, 
                               library_dirs=pj_lib_dirs, 
                               libraries=pj_libs,
                               extra_link_args=extra_link_args,
                               extra_compile_args=['-Wno-missing-braces'],
                              )
                    ],
      cmdclass=versioneer.get_cmdclass()
)
