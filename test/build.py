from distutils.core import setup
import py2exe

py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "bundle_files": 1}

setup(
    options = {"py2exe": py2exe_options},
    console = [
        {
            "script" : "basictest.py",
            "icon_resources": [(1,"basictest.ico")],
        }
    ],
    zipfile = None)
