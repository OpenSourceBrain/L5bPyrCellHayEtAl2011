#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2022 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import logging


import neuroml
from neuroml.loaders import read_neuroml2_file
from pyneuroml.plot import PlotMorphology
from pyneuroml.utils import component_factory
from pyneuroml.pynml import write_neuroml2_file, run_lems_with_jneuroml_neuron
from pyneuroml.lems.LEMSSimulation import LEMSSimulation


# Set up a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def model(show_cell_morph: bool = False) -> None:
    """Main model function

    :param show_cell_morph: toggle to display cell morphology
    :type show_cell_morph: bool
    """
    if show_cell_morph:
        # Plot morphology of cell
        PlotMorphology.plot_2D("L5PC.cell.nml", nogui=False)

    # Read the cell, with its includes (channels)
    doc = read_neuroml2_file("L5PC.cell.nml", include_includes=True, verbose=False)
    l5pc_cell = doc.cells[0]
    # get all biophysical properties
    # l5pc_cell.biophysical_properties.membrane_properties.info(show_contents=True)

    # remove all channels from the cell
    l5pc_cell.biophysical_properties.membrane_properties.channel_density_nernsts = []
    l5pc_cell.biophysical_properties.membrane_properties.channel_density_non_uniforms = []
    l5pc_cell.biophysical_properties.membrane_properties.channel_density_non_uniform_nernsts = []
    l5pc_cell.biophysical_properties.intracellular_properties.species = []

    # confirm membrane properties is empty
    passive_cds = []
    for cd in l5pc_cell.biophysical_properties.membrane_properties.channel_densities:
        if "pas_" in cd.id:
            passive_cds.append(cd)
    l5pc_cell.biophysical_properties.membrane_properties.channel_densities = passive_cds
    l5pc_cell.info(show_contents=True)
    l5pc_cell.biophysical_properties.membrane_properties.info(show_contents=True)
    l5pc_cell.biophysical_properties.intracellular_properties.info(show_contents=True)

    # could also have replaced the cell in the original doc with this one, but this
    # is perhaps cleaner (and leaner)
    newdoc = component_factory("NeuroMLDocument", id="L5PC_passive")

    # TODO: IncludeType does not extend BaseWithoutId
    pass_include = neuroml.IncludeType(href="pas.channel.nml")
    newdoc.includes.append(pass_include)

    newdoc.add(l5pc_cell)

    newnet = component_factory("Network", id="L5PC_passive_net")
    newdoc.add(newnet)
    pop = component_factory("Population", id="L5PC_passive_pop",
                            component=l5pc_cell.id,
                            size=1)
    newnet.add(pop)

    # add inputs, create simulation
    # helper method to quickly add input stimulus, similar to how we have utils
    # for adding bits to a cell?
    # Declare new input PulseGenerator
    input_stim = component_factory("PulseGenerator", id="IClamp", delay="5ms",
                                   duration="50ms", amplitude="0.002nA")
    newdoc.add(input_stim)

    inputlist = component_factory("InputList", id="IClampInput",
                                  component="IClamp",
                                  populations="L5PC_passive_pop")
    input_ = component_factory("Input", id=0,
                               target="../L5PC_passive_pop/0/L5PC",
                               destination="synapses")
    inputlist.add(input_)
    newnet.add(inputlist)

    print(newdoc.summary())
    write_neuroml2_file(newdoc, "l5pc_passive_test.nml", validate=True)


def sim() -> None:
    """Simulate model"""
    sim = LEMSSimulation("L5PC_passive_sim", 100, 0.01,
                         target="L5PC_passive_net")
    sim.include_neuroml2_file("l5pc_passive_test.nml")
    fname = sim.save_to_file()
    run_lems_with_jneuroml_neuron(fname, nogui=True)


if __name__ == "__main__":
    model()
    sim()
