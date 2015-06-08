
import matplotlib.pyplot as pylab

chans = ['NaTa_t']

gates = ['m', 'h']

for channel_id in chans:
    
    fig = pylab.figure()
    fig.canvas.set_window_title("Time Course(s) of activation variables of %s"%(channel_id))

    pylab.xlabel('Membrane potential (V)')
    pylab.ylabel('Time Course - tau (s)')
    pylab.grid('on')

    for gate in gates:
        vramp_lems_file  = '%s.rampV.lems.dat'%(channel_id)
        
        ts = []
        volts = []
        for line in open(vramp_lems_file):
            ts.append(float(line.split()[0])*1000)
            volts.append(float(line.split()[1])*1000)
            
        tau_lems_file  = '%s.%s.tau.lems.dat'%(channel_id, gate)
        taus = []
        for line in open(tau_lems_file):
            ts.append(float(line.split()[0])*1000)
            taus.append(float(line.split()[1])*1000)
        
        pylab.plot(volts, taus, linestyle='-', label="LEMS %s %s tau"%(channel_id, gate))
        
        tau_mod_file  = 'mods/%s.%s.tau.dat'%(channel_id, gate)
        vs = []
        taus = []
        for line in open(tau_mod_file):
            vs.append(float(line.split()[0]))
            taus.append(float(line.split()[1]))
        
        pylab.plot(vs, taus, linestyle='-', label="Mod %s %s tau"%(channel_id, gate))

    pylab.legend()
    
pylab.show()
