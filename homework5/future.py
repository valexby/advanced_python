#!/usr/bin/env python3
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import sys
import time


def check_primary(n):
    n, primes = n
    threshold = int(n ** 0.5)
    for prime in primes:
        if prime > threshold:
            break
        if n % prime == 0:
            return False, n
    return True, n


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    is_primes = []
    primes = []
    pool = ProcessPoolExecutor(multiprocessing.cpu_count())
    for i in range(2, end):
        while not all(future.done()
                      for future in is_primes[:round(int(i ** 0.5))]):
            time.sleep(0.01)
        is_primes.append(pool.submit(check_primary, (i, primes)))
        is_primes[-1].add_done_callback(
            lambda f: primes.append(f.result()[1]) if f.result()[0] else None
        )

    while not all(future.done() for future in is_primes):
        time.sleep(0.01)
    primes = [prime for prime in primes if prime >= start]
    print(sorted(primes))


if __name__ == "__main__":
    main()
