#!/usr/bin/env python3
"""Processes synchronisation example script
"""
from multiprocessing import Process
from multiprocessing import Pipe


def proc(is_eval, connection):
    """Process body
    """
    if is_eval:
        print(connection.recv())
    for number in range(int(is_eval), 100, 2):
        connection.send(number)
        print(connection.recv())
    connection.send(100)


def main():
    """Main function
    """
    connection1, connection2 = Pipe(duplex=True)
    process1 = Process(target=proc, args=(False, connection1))
    process2 = Process(target=proc, args=(True, connection2))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


if __name__ == "__main__":
    main()
