from scanparams import *
import os

for masses in QvGammav_masses:
    command = 'python python/whip_production.py HiddenValley_mQ%dmGamma%d'%(masses[0], masses[1])+' 5000 10'
    print command
