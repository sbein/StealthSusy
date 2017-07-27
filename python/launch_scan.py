from scanparams import *
import os

testmode = True
dogluino = True
dosquark = False

if testmode:
  if dosquark:
    for masses in SquarkSinglinoSinglet_masses[:1]:
        command = 'python StealthSusy/python/whip_production.py HVSusySqSq_mSq%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2])+' 10 10'
        command = command.replace('_cff.py','')
        print command
  if dogluino:        
    for masses in GluinoSinglinoSinglet_masses[:1]:
        command = 'python StealthSusy/python/whip_production.py HVSusyGluGlu_mGlu%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2])+' 10 10'
        command = command.replace('_cff.py','')
        print command

else:
  if dosquark:            
    for masses in SquarkSinglinoSinglet_masses:
        command = 'python StealthSusy/python/whip_production.py HVSusySqSq_mSq%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2])+' 100 100'.replace('_cff.py','')
        command = command.replace('_cff.py','')
        print command
        os.system(command)
  if dogluino:        
    for masses in GluinoSinglinoSinglet_masses:        
        command = 'python StealthSusy/python/whip_production.py HVSusyGluGlu_mGlu%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2])+' 100 100'.replace('_cff.py','')
        command = command.replace('_cff.py','')
        print command
        os.system(command)        
