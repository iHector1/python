import sys

print(sys.path)

import re

text= 'Mi numeor de telefono 311 355 38 50, el codigo del pais es 57, minumero de la uete es 3'
result= re.findall('[0-9]+',text)
print(result)

import time

timestamp= time.time()
local= time.localtime()
result2=time.asctime(local)
print(result2)