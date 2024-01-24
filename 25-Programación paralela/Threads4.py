#######################################
#       Fichero: Threads4.py          #
#     Crea diferentes threads         #
#######################################

import time
import threading

def worker():
    print('Hilo:',threading.current_thread().getName(),'con identificador:', threading.current_thread().ident)

HILOS = 5

for num_hilo in range(HILOS):
    hilo = threading.Thread(name = 'hilo %s' %num_hilo,target=worker)
    hilo.start()

