#######################################
#         Fichero: Proc1.py           #
#     Crea diferentes procesos        #
#######################################

import os
import time
import threading
import multiprocessing

def worker():
    print("PID: %s, Nombre proceso: %s, Nombre hilo: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name))

worker()

proceso1 = multiprocessing.Process(target=worker)
proceso2 = multiprocessing.Process(target=worker)
proceso1.start()
proceso2.start()
proceso1.join()
proceso2.join()
