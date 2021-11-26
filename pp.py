import queue
import math
import concurrent.futures
from multiprocessing import Process
import tkinter as tk


def putting_queue(q1, num_of_el):
    ii = 0
    while True:
        ii += 1
        # print('starting thread')
        # putting an e^2 every 5 seconds
        # time.sleep(2)
        q1.put_nowait(math.exp(ii))
        # print(f'put e^2 ------- {ii}. time')
        # time.sleep(1)
        if ii == num_of_el:
            break


def ququ1():
    qq = queue.Queue()
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     qq = executor.map(putting_queue(qq, 3))
    putting_queue_process = Process(target=putting_queue(qq, 3))
    putting_queue_process.start()
    putting_queue_process.join()
    return qq


def getting_thread(qqq):
    m = []
    while not qqq.empty():
        m.append(qqq.get())
    return m


# print(getting_thread(ququ1()))


class MyApp(tk.Tk):
    """The app"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("The elements of the queue -> in a list ^^ ")
        self.geometry('400x200')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.app_data = {"q_elements": getting_thread(ququ1())}

        container = tk.Frame(self)
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg="#0D5176")

        frame = tk.Frame(self, padx=50, pady=50)
        frame.pack()

        frame1 = FrameOne(parent=container, controller=self)
        frame1.pack()


class FrameOne(tk.Frame):
    """ The only frame """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.config(bg="#EA4C46")

        self.i = -1

        self.label1 = tk.Label(self, pady=40, bg="#0D98BA", font='Helvetica 24  bold',
                               borderwidth=10, relief="raised")
        self.label1.pack()
        self.every5sec()

    def every5sec(self):
        self.i += 1
        if self.i == len(self.controller.app_data["q_elements"]):
            return
        self.label1['text'] = self.controller.app_data["q_elements"][self.i]
        self.after(5000, self.every5sec)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()