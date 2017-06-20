import os, sys

dirStem=os.getcwd()
print 'DIRSTEM=',dirStem

try: sigid = sys.argv[1].replace('.slha','')
except: sigid = 'HiddenValleyAll'
try: numevents = int(sys.argv[2])
except: numevents = 3
try: numjobs = int(sys.argv[3])
except: numjobs = 1


if not os.path.exists('CMSSW_8_0_5_patch1/src/Configuration/Generator/python/'+sigid+'_cff.pyc'):
	print 'no frag called CMSSW_8_0_5_patch1/src/Configuration/Generator/python/'+sigid+'_cff.pyc'
	exit(0)

if not os.path.exists('loot.tar'):
    print 'creating a new tar file'
    os.system('tar -cvf loot.tar CMSSW_8_0_5_patch1')
else: print 'using existing tar file'

JDLtemplate = open(dirStem+'/template.jdl')
JDLtemplines = JDLtemplate.readlines()
JDLtemplate.close()

SHtemplate = open(dirStem+'/template.sh')
SHtemplines = SHtemplate.readlines()
SHtemplate.close()

for nj in range(1,numjobs+1):
	job = 'job_'+sigid+'_'+str(nj)+'of'+str(numjobs)
	print 'creating jobs:',job

	newjdl = open('jobs/'+job+'.jdl','w')
	for jdlline in JDLtemplines:
		if 'template' in jdlline:
			jdlline = jdlline.replace('template', job)
		newjdl.write(jdlline)
	newjdl.close()
	newsh = open('jobs/'+job+'.sh','w')
	for shline in SHtemplines:
		if 'template' in shline:
			shline=shline.replace('template',job)
		if 'WORKINGDIR' in shline:
			shline=shline.replace('WORKINGDIR',dirStem)            
		if 'SIGID' in shline:
			shline=shline.replace('SIGID',sigid)
		if '_n0' in shline:
			shline=shline.replace('_n0','_'+str(nj)+'of'+str(numjobs))
		if 'NUMEVENTS' in shline:
			shline=shline.replace('NUMEVENTS',str(numevents))
		newsh.write(shline)
	newsh.close()

	cmd =  'condor_submit jobs/'+job+'.jdl'
	print cmd
	os.system(cmd)
    
print 'done'
