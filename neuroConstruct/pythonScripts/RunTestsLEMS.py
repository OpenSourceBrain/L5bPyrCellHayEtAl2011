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

simConfigs.append("TestNeuroML")

simDt =                 0.001

simulators =            ["NEURON", "LEMS"]

varTimestepNeuron =     False
varTimestepTolerance =  0.0001

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
                                      verbose = verbose,
                                      numConcurrentSims = 2)

    simManager.runMultipleSims(simConfigs =           simConfigs,
                               simDt =                simDt,
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron,
                               varTimestepTolerance = varTimestepTolerance)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          analyseSims =       analyseSims)

    # These were discovered using ../../NEURON/test.py WITH DT = 0.001

    times = [306.303, 320.052, 334.602, 349.882, 365.473, 381.181, 396.932]
    spikeTimesToCheck = {'CG_TestCML_0': times}
    
    spikeTimeAccuracy = 0.1

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


