# StealthSusy

git clone https://github.com/sbein/StealthSusy.git

cp StealthSusy/template.sh .

cp StealthSusy/template.jdl .

cmsrel CMSSW_8_0_5_patch1

cd CMSSW_8_0_5_patch1/src

cmsenv

git-cms-addpkg Configuration/Generator

git-cms-addpkg PhysicsTools/PatAlgos

cp ../../StealthSusy/PhysicsTools/PatAlgos/python/slimming/prunedGenParticles_cfi.py  PhysicsTools/PatAlgos/python/slimming/

cp -r ../../StealthSusy/Configuration/Generator/python/StealthSqSq_test_cff.py Configuration/Generator/python

cmsenv

scram b 

cd ../../

cmsDriver.py StealthSqSq_test_cff --conditions auto:run2_mc --fast --era Run2_2016 --eventcontent AODSIM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO,EI,HLT:@relval25ns --datatier AODSIM --beamspot Realistic50ns13TeVCollision --fileout StealthSqSq_test_AODSIM_n0.root --no_exec -n 10

cmsRun StealthSqSq_test_cff_GEN_SIM_RECOBEFMIX_DIGI_L1_DIGI2RAW_L1Reco_RECO_EI_HLT.py

cmsDriver.py step3 --conditions auto:run2_mc --fast --eventcontent MINIAODSIM --runUnscheduled --filein file:StealthSqSq_test_AODSIM_n0.root -s PAT --datatier MINIAODSIM --era Run2_25ns --mc --fileout StealthSqSq_miniAODSIM_n0.root -n 10
