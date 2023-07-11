# https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3

import os
print(os.getcwd()) #muestra la ruta desde donde se ejecuta el programa
print(os.listdir('.'))

path = '/home/marcos/cac_python/08-Archivos/days.txt'
new_path = '/home/marcos/cac_python/08-Archivos/new_days.txt'
title = 'Days of the Week\n'

with open(path,'r') as days_file, open(new_path,'w') as new_days:
    days = days_file.read()
    
    new_days.write(title)
    new_days.write(days)
    
    print(title)
    print(days)
