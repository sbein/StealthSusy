import os
from glob import glob

sourcedir = '/eos/uscms//store/user/sbein/StealthSusy/Production/ntuple/smallchunks/*'
flist = glob(sourcedir)
uniquestems = []
for fname in flist:
    if '27_2009' in fname: continue
    stem = fname.split('_ntuple_')[0]
    if not (stem in uniquestems): uniquestems.append(stem)

for stem in uniquestems:
    newfile = stem.replace('_','')
    newfile = newfile.replace('pMSSM12MCMC1','pMSSM_mMother-')
    newfile = newfile+'_mLSP-0_fast.root'
    command = 'hadd -f '+newfile.replace('/smallchunks','') + ' ' + stem+'*.root'
    print command
    os.system(command)

