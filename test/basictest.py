# -*- coding: utf-8 -*-

""" basictest

Copyright 2013 kuma.amatsuki@gmail.com
"""

import suzunari

class BasicTest(suzunari.Base):

    def test01(self):
        self.dlog("test01")
        self.log("Ichigo")
        self.elog("No error")

def main():
    test = BasicTest(1)
    test.test01()

if __name__ == '__main__':
    main()
