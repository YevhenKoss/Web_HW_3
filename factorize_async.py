from time import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for factor in range(1, number + 1):
            if number % factor == 0:
                factors.append(factor)
        result.append(factors)
    return result


def callback(result):
    a = result[0][0]
    b = result[1][0]
    c = result[2][0]
    d = result[3][0]
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]


if __name__ == '__main__':
    # print(cpu_count())
    start_time = time()
    with Pool(cpu_count()) as p:
        p.map_async(factorize, [128, 255, 99999, 10651060], callback=callback)
        p.close()
        p.join()
    end_time = time()
    total = end_time - start_time
    print(total)
