# -*- coding: utf-8 -*-

""" physical

Copyright 2013 masaki.noda@gmail.com
"""

import time

import suzunari

# PhysicalLayer
class PhysicalLayer(suzunari.Node):
    """ physical layer """

    def __init__(self, debug_level=0):
        suzunari.Node.__init__(self, debug_level)
        self._buffer = ""

    # Node interface

    def loop_init(self):
        return True

    def loop_proc(self):
        self.dlog("*")
        time.sleep(0.5)

    def loop_clean(self):
        return

    # Physical layer interface

    def send_data(self, data):
        pass

    def receive_data(self, data):
        if not isinstance(data, str):
            return -1
        if not self.push_buffer(data):
            return -1
        return len(data)

    def received_data(self, data):
        self.dlog("Recv %s" % data)
        return len(data)


#
# Test
#

def main():
    node = PhysicalLayer(1)
    node.start()
    time.sleep(2)
    node.stop()

if __name__ == '__main__':
    main()

