# import multiprocessing
import concurrent.futures
import pickle
import time


def do_something(seconds):
    print(f' Sleeping {seconds} second ')
    time.sleep(seconds)
    return f'Done sleeping {seconds}'

def myapp():

    start = time.perf_counter()

    #
    # p1 = multiprocessing.Process(target=do_something())
    # p2 = multiprocessing.Process(target=do_something())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, sec) for sec in range(10)]
        results = executor.map(do_something, secs)

        # for result in results:
        #     print(result)


        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result())
        # print(f2.result())

    # processes = []
    #
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()

    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

# do_something()
# do_something()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    myapp()
