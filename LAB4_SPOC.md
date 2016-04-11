#LAB4 SPOC
计32 龙浩民  2013011319

## 13.1 总体介绍

### (1) ucore的线程控制块数据结构是什么？

`proc_struct`，定义如下：

	struct proc_struct {
    	enum proc_state state;                      // Process state
	    int pid;                                    // Process ID
	    int runs;                                   // the running times of Proces
	    uintptr_t kstack;                           // Process kernel stack
    	volatile bool need_resched;                 // bool value: need to be rescheduled to release CPU?
    	struct proc_struct *parent;                 // the parent process
	    struct mm_struct *mm;                       // Process's memory management field
	    struct context context;                     // Switch here to run process
		struct trapframe *tf;                       // Trap frame for current interrupt
	    uintptr_t cr3;                              // CR3 register: the base addr of Page Directroy Table(PDT)
	    uint32_t flags;                             // Process flag
	    char name[PROC_NAME_LEN + 1];               // Process name
	    list_entry_t list_link;                     // Process link list 
	    list_entry_t hash_link;                     // Process hash list
	};
	
## 13.2 关键数据结构

### (2) 如何知道ucore的两个线程同在一个进程？

如果两个线程的`cr3`、`mm`都相同的话，它们都在同一个进程里；反之不是。

### (3) context和trapframe分别在什么时候用到？

`context`用于一般情况下的进程的切换。

`trapframe`用在线程的初次生成。

### (4) 用户态或内核态下的中断处理有什么区别？在trapframe中有什么体现？

用户态到内核态会有特权级的变换。

`trapframe`中会多压入`ss`与`esp`（用户栈）。

## 13.3 执行流程

### (5) do_fork中的内核线程执行的第一条指令是什么？它是如何过渡到内核线程对应的函数的？

`/kern/process/entry.S`中的`pushl %edx`；过度到内核线程：

	 tf.tf_eip = (uint32_t) kernel_thread_entry; 
	 
### (6)内核线程的堆栈初始化在哪？

参见`tf`和`context`中的`esp`初始化代码。

### (7) fork()父子进程的返回值是不同的。这在源代码中的体现中哪？ 

父进程调用`fork()`的时候，`ret = proc->pid;`， 可知父进程能得到子进程的pid。

子进程在`do_fork()`中调用`copy_thread()`时，`proc->tf->tf_regs.reg_eax = 0`，说明子进程返回值为0。

### (8) 内核线程initproc的第一次执行流程是什么样的？能跟踪出来吗？

第一次执行`cpu_idle()`后，`initproc`被调度；

在`schedule()`中	，调用了`proc_run()`完成了上下文切换。
	 
	
