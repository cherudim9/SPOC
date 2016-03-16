def init_storage(filename):
    i=0
    storage=[]
    for line in open(filename).readlines():
        if line.replace('\n','')=='':
            continue
        tmp=(line.split(':')[1]).replace('\n','').split(' ')
        tmp1=[]
        for a in tmp:
            if a!='':
                tmp1.append(a)
        tmp=map(lambda x: int(x,16), tmp1)
        storage.append(tmp)
        i=i+1
    return storage

phy=init_storage('phy.txt')
disk=init_storage('disk.txt')

while True:
    vir=int(raw_input().replace('0x',''),16)
    print 'virtual address %s' % (hex(vir))

    pde_index= (vir>>10)
    pde = phy[int('6c',16)][pde_index] #6c
    d_valid= (pde>>7)
    pde_pt= pde - (d_valid<<7)
    print '\t--> pde index: %s\tpde contents: (valid %d, pfn %s)' % ( hex(pde_index), d_valid, hex(pde_pt) )
    if (d_valid==0):
        print '\t\tFault (page directory entry not valid)'
        continue

    pte_index=(vir>>5)&0x1f
    pte = phy[pde_pt][pte_index]
    pfn = (pte&~(1<<7))
    t_valid= (pte>>7)

    if t_valid==0 and pfn==int('1f',16):
        print '\t\t--> nothing'
        continue

    print '\t\t--> pte index: %s\tpde contents: (valid %d, pfn %s)' % (hex(pte_index), t_valid, hex(pfn) )
    addr=(pfn<<5)+(vir&0x1f)
    if (t_valid==0):
        print '\t\t\t--> To Disk Sector Address %s --> Value: %s' %( hex(addr), hex(disk[pfn][vir&0x1f]) )
        continue

    print '\t\t\t--> To Physical Address %s --> Value: %s' % ( hex(addr), hex(phy[pfn][vir&0x1f]) )
