import multiprocessing


# result = []

def calc_square(nums, q):
    # global result
    for n in nums:
            # result.append(n*n)
        q.put(n*n)
    # print(' inside process '+str(result))

def main():
    nums = range(10)
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(nums, q))

    p.start()
    p.join()

    # print('outside process '+ str(result))
    while not q.empty():
        print(q.get())





if __name__ == '__main__':
    main()