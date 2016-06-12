#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk)
plt.title("Random walk with +1/-1 steps")

plt.show()

