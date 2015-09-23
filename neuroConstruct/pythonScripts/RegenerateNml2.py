import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using ..\\..\\..\\nC.bat -python XXX.py' or '../../../nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc # Many useful functions such as SimManager.runMultipleSims found here

projFile = File(os.getcwd(), "../L5bPyrCellHayEtAl2011.ncx")

simConfigs = []
simConfigs.append("TestNeuroML")

nc.generateNeuroML2(projFile, simConfigs)

extra_files = ['.test*',
               'cell2_fromNeurolucida.nml', 
               'CaDynamics_E2_NML2*gamma*.nml', 
               'L5PC.cell.nml', 
               '*TestL5PC*ml',
               'analyse_chans.sh',
               'compare_nml2_mods.py',
               'mods']
if len(sys.argv)==2 and sys.argv[1] == "-f":
    extra_files.append('L5bPyrCellHayEtAl2011.net.nml')
    extra_files.append('LEMS_L5bPyrCellHayEtAl2011.xml')
    extra_files.append('LEMS_L5bPyrCellHayEtAl2011_LowDt.xml')
    
from subprocess import call
for f in extra_files:
    call(["git", "checkout", "../generatedNeuroML2/%s"%f])

quit()
