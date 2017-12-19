from ROOT import *

f = TFile('StealthSqSq_miniAODSIM_n0.root')

Events = f.Get('Events')

#Events.Show(0)

Events.Draw("recoGenParticles_prunedGenParticles__PAT.obj.m_state.pdgId_","recoGenParticles_prunedGenParticles__PAT.obj.m_state.pdgId_>3000000","hist")

c1.Update()

def pause(thingy='please push enter'):
    import sys
    print thingy
    sys.stdout.flush()
    raw_input('')
pause()
