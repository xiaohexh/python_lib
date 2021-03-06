#!/usr/bin/env python
#coding=utf-8

from blinker import Signal

class Processor:
    def __init__(self, name):
        self.name = name

    def go(self):
        ready = Signal("ready")
        ready.send(self)
        complete = Signal("complete")
        complete.send(self)

    def __repr__(self):
        return "%s" % self.name


if __name__ == "__main__":
    processor_a = Processor("a")
    processor_a.go()
