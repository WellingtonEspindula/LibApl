#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt
import math as m

pi = np.pi
norm = np.linalg.norm
vetorial = np.cross
escalar = np.dot

def resolucao(rl, rll, rlll):
    return [["torcao", torcao(rl, rll, rlll)],
             ["curvatura", curvatura(rl, rll)],
             ["aceleracao_normal", aceleracao_norm(rl,rll)],
             ["aceleracao_tangencial", aceleracao_tan(rl, rll)]]

def torcao(rl, rll, rlll):
    """ rl eh a derivada primeira da curva r(t) no tempo t 
        rll eh a derivada segunda
        rlll eh a derivada terceira
    """
    return misto(rl, rll, rlll)/(norm(vetorial(rl, rll))**2)

def curvatura(rl, rll):
    """ rl eh a derivada primeira da curva r(t) no tempo t 
        rll eh a derivada segunda
    """
    return norm(vetorial(rl, rll))/(norm(rl)**3)

def aceleracao_norm(rl, rll):
    """ rl eh a derivada primeira da curva r(t) no tempo t 
        rll eh a derivada segunda
    """
    return norm(vetorial(rll, rl))/norm(rl)

def aceleracao_tan(rl, rll):
    """ rl eh a derivada primeira da curva r(t) no tempo t 
        rll eh a derivada segunda
    """
    return (escalar(rll, rl))/norm(rl)

def misto(u, v, w):
    return np.cross(u,v).dot(w)

def arr(*args):
    return np.array(args)
