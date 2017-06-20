from scanparams import *
import os

testmode = False

if testmode:
    for masses in SinglinoSinglet_masses[:1]:
        command = 'python StealthSusy/python/whip_production.py StealthSqSq_mSinglino%dmSinglet%d'%(masses[0], masses[1])+' 10 10'
        print command

else:
    for masses in SinglinoSinglet_masses:
        command = 'python StealthSusy/python/whip_production.py StealthSqSq_mSinglino%dmSinglet%d'%(masses[0], masses[1])+' 10000 10'
        print command
        os.system(command)
