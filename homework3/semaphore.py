import threading


def print_number(is_odd, lock_me, lock_neigbour):
    lock_me.acquire()
    for i in range(int(is_odd), 100, 2):
        print(i)
        lock_neigbour.release()
        lock_me.acquire()


def main():
    lock1 = threading.Semaphore()
    lock2 = threading.Semaphore()
    lock1.acquire()
    lock2.acquire()
    thread1 = threading.Thread(target=print_number, args=[False, lock1, lock2])
    thread2 = threading.Thread(target=print_number, args=[True, lock2, lock1])
    thread1.start()
    thread2.start()
    lock1.release()
    thread1.join()
    lock2.release()
    thread2.join()


if __name__ == "__main__":
    main()
