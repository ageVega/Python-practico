#######################################
#       Fichero: Threads2.py          #
#     Crea diferentes threads         #
#######################################

import threading

def worker():
    print('Hilo:',threading.current_thread().getName(),'con identificador:', threading.current_thread().ident)

worker()
worker()

hilo1 = threading.Thread(target=worker)
hilo2 = threading.Thread(target=worker)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()


