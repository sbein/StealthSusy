from scanparams import *

#template_frag = 'StealthSusy/Configuration/Generator/python/StealthSqSq_test_cff.py'
for modelkey in template_frags:

   ftemplate = open(template_frags[modelkey])
   lines = ftemplate.readlines()
   ftemplate.close()

   for masses in masspoints:
           ftemp = template_frags[modelkey].split('/')[-1]
           fname = ftemp.replace('template','MM%d_MSo%d_MSt%d'%(masses[0], masses[1],masses[2]))
           fragdir = 'CMSSW_8_0_5_patch1/src/Configuration/Generator/python'
           f = open(fragdir+'/'+fname,'w')
           print 'creating', fragdir+'/'+fname
           for line in lines:
               line = line.replace(' %MMOTHER% ',' '+str(masses[0])+' ')
               line = line.replace(' %MSINGLINO% ',' '+str(masses[1])+' ')
               line = line.replace(' %MSINGLET% ',' '+str(masses[2])+' ')
               line = line.replace(' %MCHI% ',' '+str(9)+' ')     
               f.write(line)
           f.close()