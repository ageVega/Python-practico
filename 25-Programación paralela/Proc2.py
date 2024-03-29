#######################################
#         Fichero: Proc1.py           #
#     Crea diferentes procesos        #
#######################################

import os
import time
import threading
import multiprocessing


def workerhilos():
    print("PID: %s, Nombre proceso: %s, Nombre hilo: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name))
    time.sleep(1)
    
def workerprocesos():
    workerhilos()
    hilo1 = threading.Thread(target=workerhilos)
    hilo2 = threading.Thread(target=workerhilos)
    hilo1.start()
    time.sleep(1)
    hilo2.start()
    hilo1.join()
    hilo2.join()

workerprocesos()

proceso1 = multiprocessing.Process(target=workerprocesos)
proceso2 = multiprocessing.Process(target=workerprocesos)
proceso1.start()
proceso2.start()
proceso1.join()
proceso2.join()
