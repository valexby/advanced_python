import threading


def print_number(is_odd, lock_me, lock_neigbour):
    lock_me.wait()
    for i in range(int(is_odd), 100, 2):
        lock_me.clear()
        print(i)
        lock_neigbour.set()
        lock_me.wait()
    lock_neigbour.set()


def main():
    event1 = threading.Event()
    event2 = threading.Event()
    event1.clear()
    event2.clear()
    thread1 = threading.Thread(target=print_number,
                               args=[False, event1, event2])
    thread2 = threading.Thread(target=print_number,
                               args=[True, event2, event1])
    thread1.start()
    thread2.start()
    event1.set()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
