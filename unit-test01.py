"""Unit test providingFunction unit test hello world."""
#file: unit_test01.py

import unittest
import hello_world

HELLO_MSG = hello_world.print_helloworld()

print(hello_world.print_helloworld())

assert HELLO_MSG == "Hello, World!"
