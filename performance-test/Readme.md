Comparing NEURON and NeuroML generated NEURON code
---------------------------------------------------

Info files
==========

The info files provide summary information about the models generated using `pyneuroml.neuron.getinfo` and `pyneuroml.neuron.morphinfo` functions.
One can use `diff` (or something like `vimdiff`) to compare the information generated from the native NEURON model, and the NeuroML2 generated NEURON model.
Some manual tweaks have been made to the NeuroML info file to make comparison easier---mechanism parameters have been moved around, but no other information was changed.
