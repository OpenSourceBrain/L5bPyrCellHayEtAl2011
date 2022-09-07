#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2022 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import logging


import numpy as np


import neuroml
from neuroml.loaders import read_neuroml2_file
from pyneuroml.plot import PlotMorphology
from pyneuroml.utils import component_factory
from pyneuroml.pynml import write_neuroml2_file, run_lems_with_jneuroml_neuron
from pyneuroml.lems.LEMSSimulation import LEMSSimulation
from pyneuroml.plot.Plot import generate_plot


# Set up a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def model(show_cell_morph: bool = False) -> bool:
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
    l5pc_cell.id = "L5PC_passive_cell"
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
    # l5pc_cell.morphology.info(show_contents=True)
    # print(l5pc_cell.get_all_segments_in_group("soma_0"))
    # print(l5pc_cell.get_ordered_segments_in_groups("soma_0",
    #                                                include_path_lengths=True))
    # l5pc_cell.biophysical_properties.membrane_properties.info(show_contents=True)
    # l5pc_cell.biophysical_properties.intracellular_properties.info(show_contents=True)

    # could also have replaced the cell in the original doc with this one, but this
    # is perhaps cleaner (and leaner)
    newdoc = component_factory("NeuroMLDocument", id="L5PC_passive")

    include = component_factory("IncludeType", href="pas.channel.nml")
    newdoc.add(include)

    newdoc.add(l5pc_cell)

    # Do not validate now because it does not contain populations etc.
    newnet = component_factory("Network", id="L5PC_passive_net", validate=False)
    newdoc.add(newnet)
    pop = component_factory("Population", id="L5PC_passive_pop",
                            component="L5PC_passive_cell",
                            type="populationList", size=1)
    # id is compulsory in Instance, but not marked so in the schema because you
    # can either have id, or you can have i, j, k which also act like an id.
    pop.add(component_factory("Instance", id=0, location=component_factory("Location", x="0", y="0", z="0")))
    newnet.add(pop)

    # add inputs, create simulation
    # helper method to quickly add input stimulus, similar to how we have utils
    # for adding bits to a cell?
    # Declare new input PulseGenerator
    input_stim = component_factory("PulseGenerator", id="IClamp", delay="700ms",
                                   duration="2000ms", amplitude="0.793nA")
    newdoc.add(input_stim)

    inputlist = component_factory("InputList", id="IClampInput",
                                  component="IClamp",
                                  populations="L5PC_passive_pop")
    input_ = component_factory("Input", id=0,
                               target="../L5PC_passive_pop/0/L5PC_passive_cell",
                               segment_id="10",
                               destination="synapses")
    # input_.info(show_contents=True)
    # return False
    inputlist.add(input_)
    newnet.add(inputlist)

    print(newdoc.summary())
    write_neuroml2_file(newdoc, "l5pc_passive_test.nml", validate=True)

    return True


def sim(run=False) -> None:
    """Simulate model"""

    if run is False:
        return
    sim = LEMSSimulation("L5PC_passive_sim", 3000, 0.01,
                         target="L5PC_passive_net")
    sim.include_neuroml2_file("l5pc_passive_test.nml")
    sim.set_report_file("report.txt")
    sim.create_output_file("l5pc_passive_output", "l5pc_passive_output.dat")
    sim.add_column_to_output_file("l5pc_passive_output",
                                  "pop[0]_v",
                                  "L5PC_passive_pop/0/soma_0/11/v")
    fname = sim.save_to_file()
    run_lems_with_jneuroml_neuron(fname, nogui=True)
    data = np.loadtxt("l5pc_passive_output.dat")
    generate_plot(xvalues=[data[:, 0]], yvalues=[data[:, 1]],
                  labels=["v(soma)"],
                  title="v(soma)")


if __name__ == "__main__":
    sim(model())
