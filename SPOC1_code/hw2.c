
/*
This program will trigger five interrupts/exceptions,
   and output A,B,C,D,E in order.
*/

#include <u.h>

enum { // page table entry flags
  PTE_P   = 0x001,       // Present
  PTE_W   = 0x002,       // Writeable
  PTE_U   = 0x004,       // User
//PTE_PWT = 0x008,       // Write-Through
//PTE_PCD = 0x010,       // Cache-Disable
  PTE_A   = 0x020,       // Accessed
  PTE_D   = 0x040,       // Dirty
//PTE_PS  = 0x080,       // Page Size
//PTE_MBZ = 0x180,       // Bits must be zero
};

int in(port)    { asm(LL,8); asm(BIN); }
out(port, val)  { asm(LL,8); asm(LBL,16); asm(BOUT); }
ivec(void *isr) { asm(LL,8); asm(IVEC); }
lvadr()         { asm(LVAD); }
stmr(int val)   { asm(LL,8); asm(TIME); }
pdir(value)     { asm(LL,8); asm(PDIR); }
spage(value)    { asm(LL,8); asm(SPAG); }
halt(value)     { asm(LL,8); asm(HALT); }

int x,i;

char pg_mem[6 * 4096]; // page dir + 4 entries + alignment

int *pg_dir, *pg0, *pg1, *pg2, *pg3;

int current;

LOADI(int x){
  asm(LL,8);
}

alltraps(){
  asm(PSHA);
  asm(PSHB);
  asm(PSHC);

  LOADI(x);
  x++;
  asm(PSHA);
  asm(POPB);
  asm(LI,1);
  asm(BOUT);

  asm(POPC);
  asm(POPB);
  asm(POPA);
  asm(RTI);
}

setup_paging()
{

  pg_dir = (int *)((((int)&pg_mem) + 4095) & -4096);
  pg0 = pg_dir + 1024;
  pg1 = pg0 + 1024;
  pg2 = pg1 + 1024;
  pg3 = pg2 + 1024;

  pg_dir[0] = (int)pg0 | PTE_P | PTE_W | PTE_U;  // identity map 16M
  pg_dir[1] = (int)pg1 | PTE_P | PTE_W | PTE_U;
  pg_dir[2] = (int)pg2 | PTE_P | PTE_W | PTE_U;
  pg_dir[3] = (int)pg3 | PTE_P | PTE_W | PTE_U;
  for (i=4;i<1024;i++) pg_dir[i] = 0;

  for (i=0;i<4096;i++) pg0[i] = (i<<12) | PTE_P | PTE_W | PTE_U;  // trick to write all 4 contiguous pages

  pdir(pg_dir);
  spage(1);
}

int t,d;

main(){
  x=64;
  ivec(alltraps);
  asm(STI);

  asm(-1); //invalid instruction

  t = *(int *)0x20000000; //bad physicall address

  t = 10; d = 0; t /= d;//divided by 0

  asm(LI, 4*1024*1024); // a = 4M
  asm(SSP); // sp = a
  setup_paging();

  pg0[50] = 0;
  pdir(pg_dir);
  t = *(int *)(50<<12); //test page fault read

  *(int *)(50<<12) = 5; //test page fault write

  asm(HALT);
}
