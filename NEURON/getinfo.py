#!/usr/bin/env python3
"""
Get info from NEURON model

File: NEURON/getinfo.py 

Copyright 2022 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import json
import yaml

from pyneuroml.neuron import morphinfo, getinfo, load_hoc_or_python_file
from neuron import h


load_hoc_or_python_file("L5PC.hoc")
h.load_file("import3d.hoc")

h("objectvar mycell")
h("strdef morphology_file")
h('morphology_file = "./morphologies/cell1.asc"')
h.load_file("./models/L5PCbiophys3.hoc")
h.load_file("./models/L5PCtemplate.hoc")
h("mycell = new L5PCtemplate(morphology_file)")


with open("NEURON-morphinfo.yaml", "w") as f:
    retval = morphinfo()
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
with open("NEURON-info.yaml", "w") as f:
    retval = getinfo(h.allsec())
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
