"""Simple Context Manager Example"""

from _10_context_manager import IContextManager


class MyContext(IContextManager):
    def __init__(self, name):
        self.name = name
        print('init', self.name)

    def __enter__(self):
        print('Starting', self.name)
        return self

    def __exit__(self, *exc):
        print('Finishing', self.name)

    def __del__(self):
        print('Destructing', self.name)


with MyContext('1') as context:
    print('Hello ContextManager', context.name)

# init 1
# Starting 1
# Hello ContextManager 1
# Finishing 1
"""Destructing because of end of the program!!!"""
# Destructing 1
