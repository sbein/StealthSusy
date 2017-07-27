from scanparams import *

template_frag = 'StealthSusy/Configuration/Generator/python/StealthSqSq_test_cff.py'

ftemplate = open(template_frag)
lines = ftemplate.readlines()
ftemplate.close()

for masses in SquarkSinglinoSinglet_masses:
    f = open('CMSSW_8_0_5_patch1/src/Configuration/Generator/python/HVSusySqSq_mSq%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2]),'w')
    for line in lines:
        line = line.replace(' %MSQ% ',' '+str(masses[0])+' ')
        line = line.replace(' %MSINGLINO% ',' '+str(masses[1])+' ')
        line = line.replace(' %MSINGLET% ',' '+str(masses[2])+' ')
        line = line.replace(' %MCHI% ',' '+str(10)+' ')        
        f.write(line)
    f.close()


template_frag = 'StealthSusy/Configuration/Generator/python/StealthGluGlu_test_cff.py'
ftemplate = open(template_frag)
lines = ftemplate.readlines()
ftemplate.close()
for masses in GluinoSinglinoSinglet_masses:
    f = open('CMSSW_8_0_5_patch1/src/Configuration/Generator/python/HVSusyGluGlu_mGlu%dmSno%dmSlt%d_cff.py'%(masses[0], masses[1],masses[2]),'w')
    for line in lines:
        line = line.replace(' %MGLU% ',' '+str(masses[0])+' ')
        line = line.replace(' %MSINGLINO% ',' '+str(masses[1])+' ')
        line = line.replace(' %MSINGLET% ',' '+str(masses[2])+' ')
        line = line.replace(' %MCHI% ',' '+str(10)+' ')        
        f.write(line)
    f.close()
