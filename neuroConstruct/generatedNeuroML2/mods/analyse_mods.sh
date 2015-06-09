# CaDynamics_E2.mod Ca_HVA.mod Ca_LVAst.mod Ih.mod Im.mod K_Pst.mod K_Tst.mod NaTa_t.mod NaTs2_t.mod Nap_Et2.mod SK_E2.mod SKv3_1.mod

pynml-modchananalysis NaTa_t -stepV 5 -temperature 6.3
pynml-modchananalysis Nap_Et2 -stepV 5 -temperature 6.3
pynml-modchananalysis K_Pst -stepV 5 -temperature 6.3
pynml-modchananalysis K_Tst -stepV 5 -temperature 6.3
pynml-modchananalysis Ca_HVA -stepV 5 -temperature 6.3
pynml-modchananalysis Ca_LVAst -stepV 5 -temperature 6.3
pynml-modchananalysis Ih -stepV 5 -temperature 6.3
pynml-modchananalysis SKv3_1 -stepV 5 -temperature 6.3

# pynml-modchananalysis SK_E2 -stepV 5 -temperature 6.3 # inf is constant => no change in state var z => can't work out tau...
pynml-modchananalysis Im -stepV 5 -temperature 6.3