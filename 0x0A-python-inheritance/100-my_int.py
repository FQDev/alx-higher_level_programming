#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
