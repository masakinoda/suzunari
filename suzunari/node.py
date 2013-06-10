# -*- coding: utf-8 -*-

""" node

Copyright 2013 kuma.amatsuki@gmail.com
"""

import time
import threading
import uuid

import base

# Public classes
__all__ = ['Node']

# Node
class Node(base.Base, threading.Thread):
    """ Communication Node class """

    def __init__(self, debug_level=0):
        base.Base.__init__(self, debug_level)
        threading.Thread.__init__(self)
        self._id = uuid.uuid4()
        self._stop_instruction = False
        self._peer = None
        self.name = "%s-%s" % (self.__class__.__name__, str(self._id)[:8])

    def run(self):
        self.dlog("START thread: %s" % self.name)
        self._stop_instruction = False
        try:
            if not self.loop_init():
                self.elog("Loop init error %s" % (self.name))
                self._stop_instruction = True
        except:
            self.elog_exc()
            self._stop_instruction = True
        while not self._stop_instruction:
            try:
                self.loop_proc()
            except:
                self.elog_exc()
        try:
            self.loop_clean()
        except:
            self.elog_exc()
        self.dlog("STOP thread: %s" % self.name)

    def stop(self, wait=2.0):
        self._stop_instruction = True
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

    def send_data(self, data):
        pass

    def receive_data(self, data):
        self.dlog("data len %d" % (len(data)))
        return len(data)

    def received_data(self, data):
        self.dlog("Recv %s" % data)
        return len(data)


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

