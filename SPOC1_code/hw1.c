#include <u.h>

int x;

uint read(){
  asm(LI,0);
  asm(BIN);
  asm(SL,4);
}

write(int x){
  asm(LL,8);
  asm(PSHA);
  asm(POPB);
  asm(LI,1);
  asm(BOUT);
}

main()
{
  for(;;){
    x=read();
    if (x!=-1){
      write(x);
      asm(HALT);
    }
  }
  asm(HALT);
}
