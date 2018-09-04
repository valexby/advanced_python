#!/usr/bin/env python
"""Python killing script"""
import sys


def killme():
    "Python killing function. Have fun."
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    killme()


if __name__ == "__main__":
    killme()
