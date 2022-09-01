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


load_hoc_or_python_file("test_step.hoc")

with open("NEURON-passive-morphinfo.yaml", "w") as f:
    retval = morphinfo()
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
with open("NEURON-passive-info.yaml", "w") as f:
    retval = getinfo(h.allsec())
    print(yaml.dump(retval, sort_keys=True, indent=4), file=f, flush=True)
