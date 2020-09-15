**This directory contains a copy of the original NEURON code for the Hay et al. 2011 
model taken from [ModelDB](http://senselab.med.yale.edu/ModelDB/ShowModel.cshtml?model=139653) 
on 23 Sept 2015, with permission.**

To run the models on Linux/Unix, follow these steps:

    # Open a terminal
    # Ensure that you are in this folder
    $ ls
    init.hoc   mod   models  'model sets'   morphologies   mosinit.hoc readme.html   README.md   screenshot1.png   screenshot2.png screenshot3.png   simulationcode

    # Compile the mod files
    $ nrnivmodl mod/*
    Creating x86_64 directory for .o files
    ....
    ....
    # This creates a new folder, x86_64, where the compiled artefacts are
    # saved.

    # Run init.hoc and follow the instructions shown in the GUI to reproduce
    # the figures as noted below
    $ nrngui init.hoc

**Below is a copy of the readme.html from the original code**

Author: Etay Hay, 2011

  Models of Neocortical Layer 5b Pyramidal Cells Capturing a Wide Range of
  Dendritic and Perisomatic Active Properties
  ([Hay et al., PLoS Computational Biology, 2011](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=21829333&dopt=Abstract)) 

NEURON models and model sets corresponding to the paper:

Demo: Either auto-launch from ModelDB or download and extract the
archive and compile the mod files (with mknrndll (mswin and mac, or
nrnivmodl (linux/unix)) and then start the simulation by the file
init.hoc.

Once the simulation is started select a button to re-create parts of
Figure 4 from the paper.  Clicking on the Fig. 4A should create an
image like:

<img src="./screenshot1.png" alt="screenshot1.png">

Likewise the Fig 4B, Fig 5A buttons should create images like these:

<img src="./screenshot2.png" alt="screenshot2.png">

<img src="./screenshot3.png" alt="screenshot3.png">

Additional information:

#### Folder: [models](models)

NEURON code models, shown in various figures

    L5PCbiophys1 - figure 1 (constrained only for BAC firing)
    L5PCbiophys2 - figure 2 (constrained only for current step firing)
    L5PCbiophys3 - figure 4 (constrained both for BAC and current step firing)
    L5PCbiophys4 - figure S5 (AP initiation at the axon)
    L5PCtemplate - general cell template

#### Folder: [simulationcode](simulationcode)

Simulation code for BAC firing or step current firing.

#### Folder: [model sets](model sets)

Model sets corresponding to various figures.
 
models_errors file: error values matrix (rows: models; columns:
     objectives)
     
models_parameters file: parameter values matrix (rows: models;
    columns: parameters) objetives file: objective names, each
    corresponding to a column in models_errors file
    
genome file: parameter names and search limits, each corresponding to
    a column in the models_parameters file
   
#### Folder: [mod](mod)

mod files of the conductance mechanisms used.

#### Folder: [morphologies](morphologies)

The three morphologies used in the paper.

20130226 added critical_frequency.hoc to simulationcode folder

20130330 critical_frequency.hoc file updated with a comment regarding a difference between 32 and 64 bit NEURON environments.

