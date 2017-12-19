from scanparams import *
import os

arg = ''
for model in models:
       for masses in masspoints:
           ftemp = template_frags[model].split('/')[-1]
           fragname = ftemp.replace('template','MM%d_MSo%d_MSt%d'%(masses[0], masses[1],masses[2])).replace('_cff.py','')
           command = 'python StealthSusy/python/whip_production.py '+fragname+' 30 500'
           print command
           os.system(command+' '+arg)
           arg = '&'