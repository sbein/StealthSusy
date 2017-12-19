models = ['StealthT2qqQQ', 'StealthT2qqGG', 'StealthT2bbQQ', 'StealthT2bbGG']
models = ['StealthT2qqGG', 'StealthT2bbGG']

masspoints = [[1200,1150,1000],[1200,1050,1000], [1200,1010,1000],[1200,650,500],[1200,550,500],[1200,510,500],\
			  [1300,1250,1100],[1300,1150,1100],[1300,1110,1100],[1300,750,600],[1300,650,600],[1300,610,600],\
			  [1400,1350,1200],[1400,1250,1200],[1400,1210,1200],[1400,850,700],[1400,750,700],[1400,710,700] ]

masspoints = [[1200,1150,1000], [1200,1010,1000],[1200,650,500],[1200,510,500]]

template_frags = {}
template_frags['StealthT2qqQQ'] = 'StealthSusy/Configuration/Generator/python/StealthT2qqQQ_template_cff.py'
template_frags['StealthT2qqGG'] = 'StealthSusy/Configuration/Generator/python/StealthT2qqGG_template_cff.py'
template_frags['StealthT2bbQQ'] = 'StealthSusy/Configuration/Generator/python/StealthT2bbQQ_template_cff.py'
template_frags['StealthT2bbGG'] = 'StealthSusy/Configuration/Generator/python/StealthT2bbGG_template_cff.py'