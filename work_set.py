import numpy

def calc(lists):
	res = []
	for i in lists:
		if not i in res:
			res.append(i)
	return res

memory=[]
window_size=4
window=[]
visit=numpy.random.randint(0,5,20)

for v in visit:
    print '@visit %d' % (v)
    if v in memory:
		print '@\thit'
    else:
        print '@\tmiss'
        memory.append(v)

	window.append(v)
    while len(window)>window_size:
        window=window[1:]
    print '#### now window: ', window

    print '#### before and after filter: ', memory,' ->',
    for m in memory:
        if not m in window:
            memory.remove(m)
    print memory
