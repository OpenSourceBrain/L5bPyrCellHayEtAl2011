#
#
#   File to test current configuration of project
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using nC.bat -python XXX.py' or 'nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc # Many useful functions such as SimManager.runMultipleSims found here

projFile = File("../L5bPyrCellHayEtAl2011.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("Default Simulation Configuration")

simDt =                 0.001

simulators =            ["NEURON"]

varTimestepNeuron =     True
varTimestepTolerance =  0.00001

plotSims =              True
plotVoltageOnly =       True
runInBackground =       True
analyseSims =           True
verbose =               True

#############################################


def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading project from "+ projFile.getCanonicalPath()


    simManager = nc.SimulationManager(projFile,
                                      verbose = verbose)

    simManager.runMultipleSims(simConfigs =           simConfigs,
                               simDt =                simDt,
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron,
                               varTimestepTolerance = varTimestepTolerance)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          analyseSims =       analyseSims)

    times = [711.84126, 720.02236, 730.20796, 745.43043, 827.08991, 929.49095, 1027.7015, \
             1122.267, 1214.1016, 1303.3449, 1390.8119, 1476.6185, 1561.1513, 1644.7155, \
             1727.3263, 1809.1266, 1890.1703, 1971.0897, 2050.8026, 2130.5578, 2210.0852, \
             2289.2517, 2368.1543, 2446.7049, 2524.948, 2603.1542, 2681.297]
             
    spikeTimesToCheck = {'CellGroup_1_0': times}
    
    spikeTimeAccuracy = 0.6

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


