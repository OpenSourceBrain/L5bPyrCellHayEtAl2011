#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2022 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import numpy as np


from pyneuroml.plot import generate_plot


neuron_soma_v = np.loadtxt("NEURON-soma-v.dat")
neuroml_soma_v = np.loadtxt("NeuroML-soma-v.dat")

generate_plot(xvalues=[neuron_soma_v[:, 0], neuroml_soma_v[:, 0]],
              yvalues=[neuron_soma_v[:, 1], neuroml_soma_v[:, 1]],
              labels=["NEURON", "NeuroML"],
              linestyles=["solid", "dashed"],
              title="v(soma)")
