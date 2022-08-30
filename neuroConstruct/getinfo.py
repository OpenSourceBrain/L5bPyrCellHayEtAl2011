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
    # manually make some tweaks to ease comparison
    # included as CaDynamics_E2_NML
    """
    del retval['mechanisms']['CaDynamics_E2']
    dicta = retval['mechanisms']['CaDynamics_E2_NML2']['parameters']
    # replace parameters suffixed by _NML2
    for key, value in dicta.items():
        if "_NML2" in key:
            new_key = key[:-5]
            dicta[new_key] = dicta.pop(key)
    """

    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
