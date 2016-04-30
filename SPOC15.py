#! /usr/bin/env python

import sys
from optparse import OptionParser
import random

parser = OptionParser()
parser.add_option("-s", "--seed", default=0, help="the random seed",
                  action="store", type="int", dest="seed")
parser.add_option("-j", "--jobs", default=4, help="number of jobs in the system",
                  action="store", type="int", dest="jobs")
parser.add_option("-l", "--jlist", default="", help="instead of random jobs, provide a comma-separated list of run times",
                  action="store", type="string", dest="jlist")
parser.add_option("-m", "--maxlen", default=10, help="max length of job",
                  action="store", type="int", dest="maxlen")
parser.add_option("-p", "--policy", default="FIFO", help="sched policy to use: SJF, FIFO, RR, RE",
                  action="store", type="string", dest="policy")
parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1,
                  action="store", type="int", dest="quantum")
parser.add_option("-c", help="compute answers for me", action="store_true", default=True, dest="solve")
parser.add_option("-R", help="status of resource usage: 0(n/a), 1(requesting), 2(occupying) (comma separated integers list)", action="store", default="", type="string", dest="resource")
parser.add_option("-P", help="the levels of priority (comma separated integers list)", action="store", default="", type="string", dest="priority")

(options, args) = parser.parse_args()

random.seed(options.seed)

print 'ARG policy', options.policy
if options.jlist == '':
    print 'ARG jobs', options.jobs
    print 'ARG maxlen', options.maxlen
    print 'ARG seed', options.seed
else:
    print 'ARG jlist', options.jlist

print ''

print 'Here is the job list, with the run time of each job: '

import operator

joblist = []

if priority == '' :
	priority = [int(i) for i in options.priority.split(',')]
else:
    priority = int(priority.split(','))

if resource == '' :
	resource = [int(i) for i in options.resource.split(',')]
else:
    resource = int(resource.split(','))

if options.jlist == '':
	for jobnum in range(0,options.jobs):
		runtime = int(options.maxlen * random.random()) + 1
		joblist.append([jobnum, runtime])
		print '  Job', jobnum, '( length = ' + str(runtime) + ' ), ',  'level of priority=', priority[jobnum], ', resource status=', resource[jobnum]
else:
    jobnum = 0
    for runtime in options.jlist.split(','):
        joblist.append([jobnum, float(runtime)])
        jobnum += 1
    for job, i in zip(joblist, range(len(joblist))):
        print '  Job', job[0], '( length = ' + str(job[1]) + ' ), ', 'priority=', priority[i], ', required resource=', resource[i]

print ''

if options.solve == True:
    print '** Solutions **\n'
    if options.policy == 'RE':

			running = resource.index(2)
			while len(priority) != 0:
				if resource[running] == 2:
					for i in range(len(resource)):
						if resource[i] == 1 and priority[i] > priority[running]:
							priority[running] = priority[i]
				if resource[running] == 1 and (2 in resource):
					running = resource.index(2)
					continue
				print "Job   ", joblist[running][0]
				joblist.pop(running)
				priority.pop(running)
				resource.pop(running)
				if priority != []:
					running = priority.index(max(priority))

else:
    print 'Compute the turnaround time, response time, and wait time for each job.'
    print 'When you are done, run this program again, with the same arguments,'
    print 'but with -c, which will thus provide you with the answers. You can use'
    print '-s <somenumber> or your own job list (-l 10,15,20 for example)'
    print 'to generate different problems for yourself.'
    print ''
