from glob import glob
import os, sys


TestMode = False

errlist = glob('jobs/logs/*.err')
nresub = 0
f2del = []
for err in errlist:
    f = open(err)
    lines = f.readlines()
    f.close()
    needsresubmitting = False
    for line in lines:
        if 'Begin Fatal Exception' in line:
            needsresubmitting = True
            break
        if '[ERROR] Server responded with an error:' in line: 
            f2del.append(err)
    if needsresubmitting:
        command = 'condor_submit '+err.replace('/logs','').replace('.err','.jdl')
        print command
        if not TestMode:
            os.system(command)
        nresub+=1
print 'need to delete root files corresponding to', f2del, 'then rerun this script'

print 'n(resub) first =',nresub
loglist = glob('jobs/logs/*.log')
nresub=0
for log in loglist:
    f = open(log)
    lines = f.readlines()
    f.close()
    needsresubmitting = False
    for line in lines:
        if 'aborted' in line: 
            needsresubmitting = True
            break
    if needsresubmitting:
        command = 'condor_submit '+log.replace('/logs','').replace('.log','.jdl')
        print command
        if not TestMode:
            os.system('rm '+log)
            os.system(command)
        nresub+=1		

print 'n(resub) abort =',nresub


