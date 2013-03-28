# -*- coding: utf-8 -*-
#
#
#   File to test project to ensure it is set up correctly 
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using 'nC.bat -python XXX.py' or 'nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

from ucl.physiol.neuroconstruct.project import ProjectManager
from ucl.physiol.neuroconstruct.project import Project
from ucl.physiol.neuroconstruct.neuron import NeuronSettings
from ucl.physiol.neuroconstruct.utils import Display3DProperties


projFile = File("../L5bPyrCellHayEtAl2011.ncx")



def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading project from "+ projFile.getCanonicalPath()
    
    projectManager = ProjectManager()
    project = projectManager.loadProject(projFile)

    assert(len(project.getProjectDescription())>0)

    assert(len(project.cellManager.getAllCells())>=12)


    #assert(project.proj3Dproperties.getDisplayOption() == Display3DProperties.DISPLAY_SOMA_SOLID_NEURITE_LINE)

    assert(project.simulationParameters.getDt()-0.025<=1e-6)

    #assert(project.neuronSettings.isVarTimeStep())

    #assert(project.neuronSettings.isForceCorrectInit())

    assert(project.neuronSettings.getDataSaveFormat().equals(NeuronSettings.DataSaveFormat.TEXT_NC))

    assert(not project.genesisSettings.isSymmetricCompartments())

    #assert(project.genesisSettings.isPhysiologicalUnits())

    assert((project.simulationParameters.getTemperature() - 6.3) < 1e-6) # Not 34!! This is needed as ModelDB scripts are run at 6.3 and this affects the Ca rev pot

    print "\n**************************************"
    print "    All tests passed!"
    print "**************************************\n"

if __name__ == "__main__":
    testAll()
    exit()