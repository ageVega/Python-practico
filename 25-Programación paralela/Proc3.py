#######################################
#         Fichero: Proc2.py           #
#     Crea diferentes procesos        #
#######################################

import os
import time
import threading
import multiprocessing

def worker(comienzo, fin):
    print("PID: %s, Nombre proceso: %s, Nombre hilo: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name))
    for valor in range(comienzo,fin,1):
        print(valor);


NUM_PROCESOS = 3

for num_proceso in range(NUM_PROCESOS):
    comienzo = num_proceso*10
    fin = 10 + num_proceso*10
    proceso = multiprocessing.Process(target=worker,args=(comienzo, fin,))
    proceso.start()
    proceso.join()
