import threading
import time


def print_number(is_odd):
    for i in range(int(is_odd), 100, 2):
        print(i)
        time.sleep(0.5)


def main():
    printer1 = threading.Thread(target=print_number, args=[False])
    printer2 = threading.Timer(0.25, print_number, [True])
    printer1.start()
    printer2.start()
    printer1.join()
    printer2.join()


if __name__ == "__main__":
    main()
