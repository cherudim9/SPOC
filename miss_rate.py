import numpy

nVISIT = 10
nPG = 5
nMEM = 3
maxMissTime = 3

if __name__=='__main__':

    visit = numpy.random.randint(0, nPG, nVISIT)

    visittime={}
    last=0
    for i in range(len(visit)):
        v = visit[i]
        print '#%d: just visited vir: %d' % (i,v)
        if v in visittime:
            visittime[v]=i
            print '\thit in mem :)'
        else:

            print '\tno hit in mem, try to swap in :('

            print '\tbefore: ', visittime

            if i - last > maxMissTime:
                print '\t\treload all'
                visittime[v]=i
                visittime=dict(filter(lambda x: x[1]>=i-maxMissTime, visittime.items()))
            else:
                print '\t\treload only one'
                visittime[v] = i
                if len(visittime)>nMEM:
                    tmp=visittime.items()
                    tmp.sort(lambda a, b: a[1]-b[1])
                    visittime = dict( tmp[1:] )

            print '\tnow dict become ', visittime
            last = i
