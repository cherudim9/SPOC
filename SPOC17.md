#SPOC 17

## 课堂思考题

当没有choosing的时候，比如说如果有两个进程：

1. 一开始num[0]=0，num[1]也等于0；
2. 然后num[1]=1；
3. 通过判断num[0]==0，进入了临界区；
4. 此时num[0]也改为1；
5. 通过条件(num[0],0)<(num[1],1)，也进入了临界区。

## 小组思考题

### 题目一
（spoc）阅读简化x86计算机模拟器的使用说明，理解基于简化x86计算机的汇编代码。

### 题目二
(spoc)了解race condition. 进入race-condition代码目录。

#### Q1 
执行`./x86.py -p loop.s -t 1 -i 100 -R dx`，请问`dx`的值是什么？

答：加上`-c`后得到（下同）：

	dx          Thread 0         
    0   
	-1   1000 sub  $1,%dx
	-1   1001 test $0,%dx
	-1   1002 jgte .top
	-1   1003 halt

所以是-1。

#### Q2

执行`./x86.py -p loop.s -t 2 -i 100 -a dx=3,dx=3 -R dx`，请问`dx`的值是什么？

答：同样都是-1：

	dx          Thread 0                Thread 1         
	3   
	2   1000 sub  $1,%dx
	2   1001 test $0,%dx
	2   1002 jgte .top
	1   1000 sub  $1,%dx
	1   1001 test $0,%dx
	1   1002 jgte .top
	0   1000 sub  $1,%dx
	0   1001 test $0,%dx
	0   1002 jgte .top
	-1   1000 sub  $1,%dx
	-1   1001 test $0,%dx
	-1   1002 jgte .top
	-1   1003 halt
	3   ----- Halt;Switch -----  ----- Halt;Switch -----  
	2                            1000 sub  $1,%dx
	2                            1001 test $0,%dx
	2                            1002 jgte .top
	1                            1000 sub  $1,%dx
	1                            1001 test $0,%dx
	1                            1002 jgte .top
	0                            1000 sub  $1,%dx
	0                            1001 test $0,%dx
	0                            1002 jgte .top
	-1                            1000 sub  $1,%dx
	-1                            1001 test $0,%dx
	-1                            1002 jgte .top
	-1                            1003 halt
	
#### Q3

`./x86.py -p loop.s -t 2 -i 3 -r -a dx=3,dx=3 -R dx`

答：依然都是-1

	dx          Thread 0                Thread 1         
	3   
	2   1000 sub  $1,%dx
	3   ------ Interrupt ------  ------ Interrupt ------  
	2                            1000 sub  $1,%dx
	2                            1001 test $0,%dx
	2                            1002 jgte .top
    2   ------ Interrupt ------  ------ Interrupt ------  
    2   1001 test $0,%dx
    2   ------ Interrupt ------  ------ Interrupt ------  
    1                            1000 sub  $1,%dx
    2   ------ Interrupt ------  ------ Interrupt ------  
    2   1002 jgte .top
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1001 test $0,%dx
    1                            1002 jgte .top
    0                            1000 sub  $1,%dx
    2   ------ Interrupt ------  ------ Interrupt ------  
    1   1000 sub  $1,%dx
    1   1001 test $0,%dx
    1   1002 jgte .top
    0   ------ Interrupt ------  ------ Interrupt ------  
    0                            1001 test $0,%dx
    1   ------ Interrupt ------  ------ Interrupt ------  
    0   1000 sub  $1,%dx
    0   1001 test $0,%dx
    0   1002 jgte .top
    0   ------ Interrupt ------  ------ Interrupt ------  
    0                            1002 jgte .top
    0   ------ Interrupt ------  ------ Interrupt ------  
	-1   1000 sub  $1,%dx
	-1   1001 test $0,%dx
	0   ------ Interrupt ------  ------ Interrupt ------  
	-1                            1000 sub  $1,%dx
	-1                            1001 test $0,%dx
	-1                            1002 jgte .top
	-1   ------ Interrupt ------  ------ Interrupt ------  
	-1   1002 jgte .top
	-1   1003 halt
	-1   ----- Halt;Switch -----  ----- Halt;Switch -----  
	-1                            1003 halt
	
#### Q4
变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -t 1 -M 2000`, 请问变量x的值是什么？

答：1。

	2000          Thread 0         
	0   
    0   1000 mov 2000, %ax
    0   1001 add $1, %ax
    1   1002 mov %ax, 2000
    1   1003 sub  $1, %bx
    1   1004 test $0, %bx
    1   1005 jgt .top
    1   1006 halt
    
#### Q5

变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -t 2 -a bx=3 -M 2000`, 请问变量x的值是什么？为何每个线程要循环3次？

答：6。两个线程，每个线程执行3次循环。

	2000          Thread 0                Thread 1         
    0   
    0   1000 mov 2000, %ax
    0   1001 add $1, %ax
    1   1002 mov %ax, 2000
    1   1003 sub  $1, %bx
    1   1004 test $0, %bx
    1   1005 jgt .top
    1   1000 mov 2000, %ax
    1   1001 add $1, %ax
    2   1002 mov %ax, 2000
    2   1003 sub  $1, %bx
    2   1004 test $0, %bx
    2   1005 jgt .top
    2   1000 mov 2000, %ax
    2   1001 add $1, %ax
    3   1002 mov %ax, 2000
    3   1003 sub  $1, %bx
    3   1004 test $0, %bx
    3   1005 jgt .top
    3   1006 halt
    3   ----- Halt;Switch -----  ----- Halt;Switch -----  
    3                            1000 mov 2000, %ax
    3                            1001 add $1, %ax
    4                            1002 mov %ax, 2000
    4                            1003 sub  $1, %bx
    4                            1004 test $0, %bx
    4                            1005 jgt .top
    4                            1000 mov 2000, %ax
    4                            1001 add $1, %ax
    5                            1002 mov %ax, 2000
    5                            1003 sub  $1, %bx
    5                            1004 test $0, %bx
    5                            1005 jgt .top
    5                            1000 mov 2000, %ax
    5                            1001 add $1, %ax
    6                            1002 mov %ax, 2000
    6                            1003 sub  $1, %bx
    6                            1004 test $0, %bx
    6                            1005 jgt .top
    6                            1006 halt
    
#### Q6
变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 0`， 请问变量x的值是什么？

答：多次运行后，发现1或者2都有可能。

1的情况：

	2000          Thread 0                Thread 1         
    0   
    0   1000 mov 2000, %ax
    0   1001 add $1, %ax
    0   ------ Interrupt ------  ------ Interrupt ------  
    0                            1000 mov 2000, %ax
    0                            1001 add $1, %ax
    1                            1002 mov %ax, 2000
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1002 mov %ax, 2000
    1   1003 sub  $1, %bx
    1   1004 test $0, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1003 sub  $1, %bx
    1                            1004 test $0, %bx
    1                            1005 jgt .top
    1                            1006 halt
    1   ----- Halt;Switch -----  ----- Halt;Switch -----  
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1005 jgt .top
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1006 halt

2的情况：

	2000          Thread 0                Thread 1         
    0   
    0   1000 mov 2000, %ax
    0   1001 add $1, %ax
    1   1002 mov %ax, 2000
    1   1003 sub  $1, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1000 mov 2000, %ax
    1                            1001 add $1, %ax
    2                            1002 mov %ax, 2000
    2   ------ Interrupt ------  ------ Interrupt ------  
    2   1004 test $0, %bx
    2   1005 jgt .top
    2   1006 halt
    2   ----- Halt;Switch -----  ----- Halt;Switch -----  
    2                            1003 sub  $1, %bx
    2   ------ Interrupt ------  ------ Interrupt ------  
    2                            1004 test $0, %bx
    2                            1005 jgt .top
    2                            1006 halt
    
#### Q7

变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 1`， 请问变量x的值是什么？

答：同上。1或者2。

#### Q8

变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -t 2 -M 2000 -i 4 -r -s 2`， 请问变量x的值是什么？

答：同上。1或者2。

#### Q9

变量x的内存地址为2000, `./x86.py -p looping-race-nolock.s -a bx=1 -t 2 -M 2000 -i 1`， 请问变量x的值是什么？

答：一直为1（因为interrupt间隔短）。

	2000          Thread 0                Thread 1         
    0   
    0   1000 mov 2000, %ax
    0   ------ Interrupt ------  ------ Interrupt ------  
    0                            1000 mov 2000, %ax
    0   ------ Interrupt ------  ------ Interrupt ------  
    0   1001 add $1, %ax
    0   ------ Interrupt ------  ------ Interrupt ------  
    0                            1001 add $1, %ax
    0   ------ Interrupt ------  ------ Interrupt ------  
    1   1002 mov %ax, 2000
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1002 mov %ax, 2000
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1003 sub  $1, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1003 sub  $1, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1004 test $0, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1004 test $0, %bx
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1005 jgt .top
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1005 jgt .top
    1   ------ Interrupt ------  ------ Interrupt ------  
    1   1006 halt
    1   ----- Halt;Switch -----  ----- Halt;Switch -----  
    1   ------ Interrupt ------  ------ Interrupt ------  
    1                            1006 halt
