# https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3

import os
print(os.getcwd()) #muestra la ruta desde donde se ejecuta el programa
print(os.listdir('.'))
path = '/home/marcos/cac_python/08-Archivos/days.txt'

with open(path,'r') as days_file:
    days = days_file.read()
    print(days)

