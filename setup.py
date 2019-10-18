#!/usr/bin/env python3
import sys, os, platform
import setuptools
from distutils.core import setup, Extension
from setuptools.command.develop import develop
from subprocess import check_call


OS_NAME = 'linux'

if sys.platform == "darwin":
    OS_NAME = 'osx'
    #os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.9'
elif sys.platform == "win32":
    if sys.maxsize > 2**32:
        OS_NAME = 'win64'
    else:
        OS_NAME = 'win32'
elif sys.platform == "linux2":
    OS_NAME = 'linux'

###########################################################
# INCLUDE_DIRS
###########################################################
INCLUDE_DIRS = []
if OS_NAME == 'win32' or OS_NAME == 'win64':
    INCLUDE_DIRS = [
        '.\\3rd_party\\ANN_static\\include',
        '.\\3rd_party\\boost_static\\include',
        '.\\3rd_party\\gdal_static\\include',
        '.\\3rd_party\\libgeoda_static\\include',
        '.\\3rd_party\\wx_static\\include',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\mswu'
    ]

else:
    INCLUDE_DIRS = [
        './3rd_party/ANN_static/include',
        './3rd_party/boost_static/include',
        './3rd_party/gdal_static/include',
        './3rd_party/libgeoda_static/include',
        './3rd_party/wx_static/include',
        './3rd_party/wx_static/lib/' + OS_NAME + '/base-unicode-static-3.0'
    ]

###########################################################
# LIBRARIES and INCLUDE_DIRS
###########################################################
LIBRARY_DIRS = []
LIBRARIES = [] # -lxxx

if OS_NAME == 'win32' or OS_NAME == 'win64':
    LIBRARIES = ['comctl32','rpcrt4']

if OS_NAME == 'linux':
    LIBRARY_DIRS += ['/usr/lib', '/usr/lib/x86_64-linux-gnu']
    LIBRARIES = []
elif OS_NAME == 'osx':
    LIBRARY_DIRS += ['/usr/lib']
    LIBRARIES = ['curl', 'iconv']

###########################################################
# SWIG_OPTS and Compiler args
###########################################################
SWIG_OPTS = ['-c++']
EXTRA_COMPILE_ARGS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_COMPILE_ARGS += ['/w']
else:
    EXTRA_COMPILE_ARGS = [
        '-std=c++11',
    ]
    if OS_NAME == 'osx':
        EXTRA_COMPILE_ARGS = [
            '-D_FILE_OFFSET_BITS=64',
            #'-mmacosx-version-min=10.9'
        ]


###########################################################
#  Link args
###########################################################
EXTRA_LINK_ARGS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_LINK_ARGS += ['/ignore:4229']

elif OS_NAME == 'osx':
    EXTRA_LINK_ARGS = [
        '-framework',
        'IOKit', 
        '-framework',
        'CoreServices',
        '-framework',
        'System',
        '-framework',
        'ApplicationServices',
        '-stdlib=libc++',
    ]

###########################################################
#  Link objects
###########################################################
EXTRA_OBJECTS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_OBJECTS = [
        '.\\3rd_party\\libgeoda_static\\lib\\' + OS_NAME + '\\geoda.lib',
        '.\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\dev\\libboost_thread-vc100-mt-1_57.lib',
        '.\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\dev\\libboost_system-vc100-mt-1_57.lib',
        '.\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\dev\\libboost_chrono-vc100-mt-1_57.lib',
        '.\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\dev\\libboost_date_time-vc100-mt-1_57.lib',
        '.\\3rd_party\\gdal_static\\lib\\' + OS_NAME + '\\dev\\gdal.lib',
        '.\\3rd_party\\gdal_static\\lib\\' + OS_NAME + '\\dev\\geos.lib',
        '.\\3rd_party\\gdal_static\\lib\\' + OS_NAME + '\\dev\\proj.lib',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\dev\\wxmsw30u.lib',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\dev\\wxregexu.lib',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\dev\\wxzlib.lib',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\dev\\wxexpat.lib',
        '.\\3rd_party\\wx_static\\lib\\' + OS_NAME + '\\dev\\wxpng.lib',
    ]

elif OS_NAME == 'linux':
    EXTRA_OBJECTS = [
        './3rd_party/libgeoda_static/lib/' + OS_NAME + '/libgeoda.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_thread.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_system.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_chrono.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_date_time.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgdal.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgeos_c.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgeos.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libproj.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libiconv.a',
        './3rd_party/wx_static/lib/' + OS_NAME + '/libwx_baseu-3.0.a',
        './3rd_party/wx_static/lib/' + OS_NAME + '/libwxregexu-3.0.a',
        './3rd_party/ANN_static/lib/' + OS_NAME + '/libANN.a',
    ]
elif OS_NAME == 'osx':
    EXTRA_OBJECTS = [
        './3rd_party/libgeoda_static/lib/' + OS_NAME + '/libgeoda.a',
        './3rd_party/ANN_static/lib/' + OS_NAME + '/libANN.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgdal.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgeos.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libgeos_c.a',
        './3rd_party/gdal_static/lib/' + OS_NAME + '/libproj.a',
        './3rd_party/wx_static/lib/' + OS_NAME + '/libwx_baseu-3.0.a',
        './3rd_party/wx_static/lib/' + OS_NAME + '/libwxregexu-3.0.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_thread.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_system.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_chrono.a',
        './3rd_party/boost_static/lib/' + OS_NAME + '/libboost_date_time.a',
    ]

###########################################################
#  Source files
###########################################################
SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp'
]

# copy _libgeoda.pyd for windows system
if OS_NAME == 'win32' or OS_NAME == 'win64':
    from shutil import copyfile
    # don't build extension on windows, which will be built in visual studio
    py_version = platform.python_version()
    if py_version.startswith('2.7'):
        copyfile('prebuild\\py27\\' + OS_NAME + '\\_libgeoda.pyd', 'pygeoda\\_libgeoda.pyd')
    elif py_version.startswith('3.7'):
        copyfile('prebuild\\py37\\' + OS_NAME + '\\_libgeoda.pyd', 'pygeoda\\_libgeoda.pyd')

###########################################################
# Extensions 
###########################################################
extensions = []
package_data = {}
include_package_data = False

###########################################################
# Utils for submodule
##########################################################
class update_submodules(develop):
    def run(self):
        print 1
        if path.exists('.git'):
            check_call(['git', 'submodule', 'update', '--init', '--recursive'])
        develop.run(self)

if OS_NAME == 'win32' or OS_NAME == 'win64':
    # don't build extension on windows, which will be built in visual studio
    package_data = {'': ['_libgeoda.pyd']}
    include_package_data = True
else:
    extensions = [Extension('pygeoda._libgeoda',
                            sources=SOURCE_FILES,
                            include_dirs=INCLUDE_DIRS,
                            swig_opts=SWIG_OPTS,
                            extra_compile_args=EXTRA_COMPILE_ARGS,
                            extra_link_args=EXTRA_LINK_ARGS,
                            library_dirs=LIBRARY_DIRS,
                            runtime_library_dirs=LIBRARY_DIRS,
                            libraries=LIBRARIES,
                            extra_objects=EXTRA_OBJECTS),]

setup (name = 'pygeoda',
       version = '0.0.3',
       author = "Xun Li",
       author_email = "lixun910@gmail.com",
       url = "https://github.com/lixun910/libgeoda",
       description = """pygeoda is a python library for spatial data analysis based on GeoDa and libgeoda.""",
       ext_modules = extensions,
       package_data = package_data,
       cmdclass = {"develop": update_submodules},
       include_package_data = include_package_data,
       packages=['pygeoda']
      )

