baseSLHATable = '''BLOCK MODSEL  # Model selection
    1     1   sugra
#
BLOCK QNUMBERS 3000001 # f
    1  0 # 3 times electric charge
    2  2 # number of spin states (2S+1)
    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)
    4  0 # Particle/Antiparticle distinction (0=own anti)
#
BLOCK QNUMBERS 3000002 # n
    1  0 # 3 times electric charge
    2  1 # number of spin states (2S+1)
    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)
    4  0 # Particle/Antiparticle distinction (0=own anti)
BLOCK MASS
   2000001     %MMOTHER% 
   2000002     %MMOTHER% 
   2000003     %MMOTHER% 
   2000004     %MMOTHER% 
   2000005     1.00000000E+10
   2000006     1.00000000E+10
   2000011     1.00000000E+10
   2000013     1.00000000E+10
   2000015     1.00000000E+10
   1000001     %MMOTHER%                 # down squark
   1000002     %MMOTHER% 
   1000003     %MMOTHER% 
   1000004     %MMOTHER% 
   1000005     1.00000000E+10
   1000006     1.00000000E+10
   1000011     1.00000000E+10
   1000012     1.00000000E+10
   1000013     1.00000000E+10
   1000014     1.00000000E+10
   1000015     1.00000000E+10
   1000016     1.00000000E+10
   1000021     1.00000000E+10
   1000022     %MCHI%                 # neutralino
   1000023     1.00000000E+10
   1000024     1.00000000E+10
   1000025     1.00000000E+10
   1000035     1.00000000E+10
   1000037     1.00000000E+10
   1000039     1.00000000E+10   #  Gravitino
   3000001     %MSINGLINO%  #  f: stealth sector
   3000002     %MSINGLET%   #  n: stealth sector
#
DECAY   2000001     0.00000000E+00
DECAY   2000002     0.00000000E+00
DECAY   2000003     0.00000000E+00
DECAY   2000004     0.00000000E+00
DECAY   2000005     0.00000000E+00
DECAY   2000006     0.00000000E+00
DECAY   2000011     0.00000000E+00
DECAY   2000013     0.00000000E+00
DECAY   2000015     0.00000000E+00
DECAY   1000001     0.00000000E+00
DECAY   1000002     0.00000000E+00
DECAY   1000003     0.00000000E+00
DECAY   1000004     0.00000000E+00
DECAY   1000005     0.00000000E+00
DECAY   1000006     0.00000000E+00
DECAY   1000011     0.00000000E+00
DECAY   1000012     0.00000000E+00
DECAY   1000013     0.00000000E+00
DECAY   1000014     0.00000000E+00
DECAY   1000015     0.00000000E+00
DECAY   1000016     0.00000000E+00

DECAY   1000021     1.00000000E+00
     1.0               3          1      -1    3000001
     
DECAY   1000001     1.00000000E+00
     1.0               2          1    3000001
     
DECAY   1000002     1.00000000E+00
     1.0               2          2    3000001
     
DECAY   1000003     1.00000000E+00
     1.0               2          3    3000001
     
DECAY   1000004     1.00000000E+00
     1.0               2          4    3000001

DECAY   1000005     1.00000000E+00
     1.0               2          5    3000001
    
DECAY   2000001     1.00000000E+00
     1.0               2          1    3000001
     
DECAY   2000002     1.00000000E+00
     1.0               2          2    3000001
     
DECAY   2000003     1.00000000E+00
     1.0               2          3    3000001
     
DECAY   2000004     1.00000000E+00
     1.0               2          4    3000001

DECAY   2000005     1.00000000E+00
     1.0               2          5    3000001
     
DECAY   3000001     1.00000000E-06   # f decays
     1.00000000e+00    2     1000022   3000002   # BR(f -> gs n )

DECAY   3000002   1.00000000E-06   # n decays
     1.00000000e+00    2          21        21   # BR(n -> g g )

DECAY   1000022     0.00000000E+00

'''

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


SLHATable = baseSLHATable.replace('%MMOTHER%','99999').replace('%MCHI%','10').replace('%MSINGLINO%','900').replace('%MSINGLET%','800').replace('%MDECAYPRODS%','1200')

generator = cms.EDFilter("Pythia8GeneratorFilter",
    #crossSection = cms.untracked.double(5.72e+07),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),
    SLHATableForPythia8  = cms.string(SLHATable),    
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:gg2squarkantisquark = on',
            'SUSY:idA = 1000001, 1000002,1000003,1000004,2000001,2000002,2000003,2000004',
            'SUSY:idB = 1000001, 1000002,1000003,1000004,2000001,2000002,2000003,2000004',          
            'print:quiet=false',
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
