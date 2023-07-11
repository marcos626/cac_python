#https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/

import glob
  
print('Named explicitly:')
for name in glob.glob('/home/marcos/lista_2.0/listas/detalles.txt'):
    print(name)
  
# Using '*' pattern 
print('\nNamed with wildcard *:')
for name in glob.glob('/home/marcos/lista_2.0/listas/*'):
    print(name)