from functools import lru_cache
import time


# use cache tool
@lru_cache()
def long_func_with_lru_cache(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


# make cache tool(memoize) by yourself
def memoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper


@memoize
def long_func_with_memoize(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


if __name__ == "__main__":
    for i in range(10):
        print(long_func_with_lru_cache(i))

    start = time.time()
    for i in range(10):
        print(long_func_with_lru_cache(i))
    print(time.time() - start)

    for i in range(10):
        print(long_func_with_memoize(i))

    start = time.time()
    for i in range(10):
        print(long_func_with_memoize(i))
    print(time.time() - start)
