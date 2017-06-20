from scanparams import *

template_frag = 'StealthSusy/GenFragments/StealthSqSq_test_cff.py'

ftemplate = open(template_frag)
lines = ftemplate.readlines()
ftemplate.close()

for masses in SinglinoSinglet_masses:
    f = open('CMSSW_8_0_5_patch1/src/Configuration/Generator/python/StealthSqSq_mSinglino%dmSinglet%d_cff.py'%(masses[0], masses[1]),'w')
    for line in lines:
        line = line.replace(' %SINGLINO% ',' '+str(masses[0])+' ')
        line = line.replace(' %SINGLET% ',' '+str(masses[1])+' ')
        f.write(line)
    f.close()
