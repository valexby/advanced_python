import threading
import time


def print_number(is_odd, cond):
    with cond:
        for i in range(int(is_odd), 100, 2):
            print(i)
            cond.notify()
            cond.wait()
        cond.notify()


def main():
    cond = threading.Condition()
    thread1 = threading.Thread(target=print_number, args=[False, cond])
    thread2 = threading.Thread(target=print_number, args=[True, cond])
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
