
phy=[]

def init_phy():
    i=0
    for line in open('phy.txt').readlines():
        if line.replace('\n','')=='':
            continue
        tmp=(line.split(':')[1]).replace('\n','').split(' ')
        tmp1=[]
        for a in tmp:
            if a!='':
                tmp1.append(a)
        tmp=map(lambda x: int(x,16), tmp1)
        phy.append(tmp)
        i=i+1

init_phy()

while True:
    vir=int(raw_input().replace('0x',''),16)
    print 'virtual address %s' % (hex(vir))

    pde_index= (vir>>10)
    pde = phy[17][pde_index]
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
    print '\t\t--> pte index: %s\tpde contents: (valid %d, pfn %s)' % (hex(pte_index), t_valid, hex(pfn) )
    if (t_valid==0):
        print '\t\t\tFault (page table entry not valid)'
        continue

    addr=(pfn<<5)+(vir&0x1f);
    print '\t\t\t-> Translates to Physical Address %s --> Value: %s' % ( hex(addr), hex(phy[pfn][vir&0x1f]) )
