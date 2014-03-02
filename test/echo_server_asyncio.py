# coding: utf-8

import asyncio
import logging

import suzunari

logging.basicConfig(level=logging.DEBUG)

class EchoProtocol(suzunari.Base):
    def connection_made(self, transport):
        print('connection_made')
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)

    def eof_received(self):
        print('eof_received')
        self.transport.close()

    def connection_lost(self, exc):
        print('connection_lost')
        if exc is not None:
            print(exc)
            self.transport.abort()
        self.transport = None

def main():
    logging.info('asyncio_test')
    loop = asyncio.get_event_loop()
    asyncio.async(loop.create_server(EchoProtocol, '127.0.0.1', 5959))
    loop.call_later(10, loop.stop)
    loop.run_forever()

if __name__ == '__main__':
    main()

