import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    #crossSection = cms.untracked.double(5.72e+07),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),
    SLHAFileForPythia8  = cms.string('SLHA/HadronicStealthAll.slha'),    
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:gg2squarkantisquark = on',
            'SUSY:qqbar2squarkantisquark = on',
            'print:quiet=false'
            'SLHA:allowUserOverride = true',  
            'SLHA:keepSM = on',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)
