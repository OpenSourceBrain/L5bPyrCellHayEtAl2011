#!/usr/bin/env python3
"""
Get info from generated NEURON files.

This *must* be run after the NEURON files have been generated from the NeuroML.

File: neuroConstruct/getinfo.py

Copyright 2022 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import json
import yaml

from pyneuroml.neuron import morphinfo, getinfo, load_hoc_or_python_file
from neuron import h


load_hoc_or_python_file("L5PC.hoc")
h("objectvar mycell")
h("strdef reference")
h('reference = "acell"')
h('mycell = new L5PC(reference, "L5PC", "A cell")')
with open("NeuroML-morphinfo.yaml", "w") as f:
    retval = morphinfo()
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
with open("NeuroML-info.yaml", "w") as f:
    retval = getinfo(h.allsec())
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
