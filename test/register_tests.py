# coding: utf-8

import sys
sys.path.append("../")
from src.register import * 

r = Register()
r.write(10,None)
print "Devia ser 10, e eh "+ str(r.get_value())

