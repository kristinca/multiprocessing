from multiprocessing import Process, Queue


def square(nums, q):
    for i in nums:
        q.put(i*i)

def cube(nums, q):
    for i in nums:
        q.put(i*i*i)

def main():

    numbers = range(5)
    queue = Queue()
    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())


if __name__ == '__main__':
    main()