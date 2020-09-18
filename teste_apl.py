#!/usr/bin/python3
# -*- coding: utf-8 -*-

import libapl as apl
import numpy as np

pi = np.pi
arr = apl.arr

# Defina aqui as suas derivadas
rl = arr(0, pi, 15)
rll = arr(4*(pi**2), 0, 4)
rlll = arr(0,-(pi**3),0)

#print(apl.resolucao(rl, rll, rlll))
print(apl.imprime_resultados(rl,rll, rlll))
