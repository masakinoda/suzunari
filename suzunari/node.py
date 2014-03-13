# -*- coding: utf-8 -*-

""" node

Copyright 2013 masaki.noda@gmail.com
"""

import uuid
import asyncio

from suzunari import base

# Public classes
__all__ = ['Node']

# Node
class Node(base.Base):
    """ Communication Node class """

    def __init__(self, debug_level=0):
        base.Base.__init__(self, debug_level)
        self.id = uuid.uuid4()
        self.name = "%s:%s" % (self.__class__.__name__, str(self.id)[:8])
        self.transport = None

    #
    # asyncio interface
    #

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            if data.startswith(b"STOP"):
                self.stop()
        except:
            self.elog_exc()

    def eof_received(self):
        self.transport.close()

    def connection_lost(self, exc):
        if exc:
            self.elog(str(exc))
        self.transport = None

    #
    # handler
    #

    def stop(self):
        loop = asyncio.get_event_loop()
        loop.call_soon(loop.stop)
 

#
# Test
#

def main():
    loop = asyncio.get_event_loop()
    asyncio.async(loop.create_server(Node, 'localhost', 8888))
    loop.call_later(10, loop.stop)
    loop.run_forever()

if __name__ == '__main__':
    main()

