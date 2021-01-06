#!/usr/bin/env python
"""
doc:
py Instead of Makefile
"""

import os


class Makefile(object):
    def __init__(self):
        self.cmd_env = 'source venv/bin/activate'
        self.cmd_test = 'venv/bin/pytest ./tests/'
        self.cmd_build = 'venv/bin/poetry build'
        self.cmd_publish = 'venv/bin/poetry publish'

    def env(self):
        os.system(self.cmd_test)

    def test(self):
        os.system(self.cmd_test)

    def build(self):
        os.system(self.cmd_publish)

    def publish(self):
        os.system(self.cmd_publish)


def main():
    make = Makefile()
    make.env()
    make.test()
    make.build()
    pass


if __name__ == '__main__':
    main()
