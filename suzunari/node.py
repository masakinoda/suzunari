# -*- coding: utf-8 -*-

""" node

Copyright 2013 masaki.noda@gmail.com
"""

import time
import threading
import uuid

from suzunari import base

# Public classes
__all__ = ['Node']

# Node
class Node(base.Base, threading.Thread):
    """ Communication Node class """

    def __init__(self, debug_level=0):
        base.Base.__init__(self, debug_level)
        threading.Thread.__init__(self)
        self._id = uuid.uuid4()
        self._stop_sign = False
        self._peer = None
        self.name = "%s:%s" % (self.__class__.__name__, str(self._id)[:8])

    def get_stop_sign(self):
        return self._stop_sign
    def set_stop_sign(self, val):
        if val:
            self._stop_sign = True
        else:
            self._stop_sign = False
    stop_sign = property(get_stop_sign)

    def run(self):
        self.dlog("START thread: %s" % self.name)
        self.set_stop_sign(False)
        # loop_init
        try:
            if not self.loop_init():
                self.elog("Loop init error %s" % (self.name))
                self.set_stop_sign(True)
        except:
            self.elog_exc()
            self.set_stop_sign(True)
        # loop
        while not self.stop_sign:
            try:
                self.loop_proc()
            except:
                self.elog_exc()
        # loop_clean
        try:
            self.loop_clean()
        except:
            self.elog_exc()
        self.dlog("STOP thread: %s" % self.name)

    def stop(self, wait=2.0):
        self.set_stop_sign(True)
        if not wait:
            return
        self.join(wait)
        if self.is_alive():
            self.elog("Join timed out %s" % self.name)

    def loop_init(self):
        return True

    def loop_proc(self):
        self.dlog(".")
        time.sleep(0.5)

    def loop_clean(self):
        return True


#
# Test
#

def main():
    obj = Node(1)
    obj.start()
    time.sleep(3)
    obj.stop()

if __name__ == '__main__':
    main()

