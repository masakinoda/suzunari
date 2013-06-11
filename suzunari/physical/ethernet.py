# -*- coding: utf-8 -*-

""" ethernet

Copyright 2013 masaki.noda@gmail.com
"""

import time

import physical

# Public classes
__all__ = ['Ethernet']

# Ethernet
class Ethernet(physical.PhysicalLayer):
    """ Ethernet physical layer """

    def __init__(self, debug_level=0):
        physical.PhysicalLayer.__init__(self, debug_level)

    # Physical layer interface

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
    node = Ethernet(1)
    node.start()
    time.sleep(2)
    node.stop()

if __name__ == '__main__':
    main()

