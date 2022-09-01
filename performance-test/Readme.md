Comparing NEURON and NeuroML generated NEURON code
---------------------------------------------------

Info files
==========

The info files in the info-comparison directory provide summary information about the models generated using `pyneuroml.neuron.getinfo` and `pyneuroml.neuron.morphinfo` functions.
One can use `diff` (or another tool like `vimdiff`) to compare the information generated from the native NEURON model, and the NeuroML2 generated NEURON model.
Some manual tweaks have been made to the NeuroML info file to make comparison easier---mechanism parameters have been moved around, but no other information was changed.

The morphology is almost identical to 4 decimal places.

The channels are also identical.
The NeuroML generated versions have extra parameters because some constants are defined as RANGE variables.

Performance
===========

Comparing performance between NeuroML generated NEURON code and native NEURON code.

Passive cell
#############

NeuroML, native NEURON
4.063438415527344, 3.0176632404327393

