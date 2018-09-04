#!/usr/bin/env python
import sys


def killme():
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    killme()


if __name__ == "__main__":
    killme()
