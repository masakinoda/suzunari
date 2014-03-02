# -*- coding: utf-8 -*-

""" base

Copyright 2013 masaki.noda@gmail.com
"""

import inspect
import logging
import os.path
import sys
import traceback

# Default logging config
logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='%(message)s',)


# Public classes
__all__ = ['Base']

# Base
class Base(object):
    """ Base class for Suzunari framework """
    
    def __init__(self, debug_level=0):
        object.__init__(self)
        self._debug_level = debug_level

    def log(self, msg):
        try:
            logging.info(msg)
        except:
            pass

    def dlog(self, msg, debug_level=1):
        try:
            if debug_level > self._debug_level:
                return
            dmsg = u"- %s (%s)" % (msg, self._get_caller())
            logging.debug(dmsg)
        except:
            pass

    def elog(self, msg):
        try:
            emsg = u"ERROR: %s (%s)" % (msg, self._get_caller())
            logging.error(emsg)
        except:
            pass

    def elog_exc(self):
        try:
            self.elog(traceback.format_exc())
        except:
            pass

    def _get_caller(self):
        name = self.__class__.__name__
        caller = inspect.stack()[2]
        fpath = os.path.basename(caller[1])
        line = caller[2]
        func = caller[3]
        return u"%s:%d %s.%s()" % (fpath, line, name, func)


#
# Test
#

def main():
    obj = Base(1)
    obj.log("Base test")
    obj.elog("Unknown error")
    obj.dlog("Debug level 1")
    obj.dlog("Debug level 2", 2)

if __name__ == '__main__':
    main()
