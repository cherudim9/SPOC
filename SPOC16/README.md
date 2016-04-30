# SPOC16 Report
计32 龙浩民 2013011319


## 修改处

`default_sched.c`的`stride_enqueue`中增加：

    cprintf("Stride_enqueue PID: %d, stride: %u\n", proc->pid, proc->lab6_stride);

`default_sched.c`的`stride_dequeue`中增加：

    cprintf("Stride_dequeue PID: %d, stride: %u\n", proc->pid, proc->lab6_stride);

`default_sched.c`的`stride_pick_next`中增加：

    cprintf("Stride_pick PID: %d, stide: %u\n", p->pid, p->lab6_stride);

`default_sched.c`的`stride_proc_tick`中增加：

    cprintf("Stride_tick PID: %d, stride: %u\n", proc->pid, proc->lab6_stride);

## 运行结果

下面的log是在stride调度算法中的相关信息。

    ++ setup timer interrupts
    Stride_pick PID: 1, stide: 2147483647
    Stride_dequeue PID: 1, stride: 2147483647
    Stride_enqueue PID: 2, stride: 0
    Stride_pick PID: 2, stide: 2147483647
    Stride_dequeue PID: 2, stride: 2147483647
    kernel_execve: pid = 2, name = "exit".
    I am the parent. Forking the child...
    Stride_enqueue PID: 3, stride: 0
    I am parent, fork a child pid 3
    I am the parent, waiting now..
    Stride_pick PID: 3, stide: 2147483647
    Stride_dequeue PID: 3, stride: 2147483647
    I am the child.
    Stride_enqueue PID: 3, stride: 2147483647
    Stride_pick PID: 3, stide: 4294967294
    Stride_dequeue PID: 3, stride: 4294967294
    Stride_enqueue PID: 3, stride: 4294967294
    Stride_pick PID: 3, stide: 2147483645
    Stride_dequeue PID: 3, stride: 2147483645
    Stride_enqueue PID: 3, stride: 2147483645
    Stride_pick PID: 3, stide: 4294967292
    Stride_dequeue PID: 3, stride: 4294967292
    Stride_enqueue PID: 3, stride: 4294967292
    Stride_pick PID: 3, stide: 2147483643
    Stride_dequeue PID: 3, stride: 2147483643
    Stride_enqueue PID: 3, stride: 2147483643
    Stride_pick PID: 3, stide: 4294967290
    Stride_dequeue PID: 3, stride: 4294967290
    Stride_enqueue PID: 3, stride: 4294967290
    Stride_pick PID: 3, stide: 2147483641
    Stride_dequeue PID: 3, stride: 2147483641
    Stride_enqueue PID: 3, stride: 2147483641
    Stride_pick PID: 3, stide: 4294967288
    Stride_dequeue PID: 3, stride: 4294967288
    Stride_enqueue PID: 2, stride: 2147483647
    Stride_pick PID: 2, stide: 4294967294
    Stride_dequeue PID: 2, stride: 4294967294
    waitpid 3 ok.
    exit pass.
    Stride_enqueue PID: 1, stride: 2147483647
    Stride_pick PID: 1, stide: 4294967294
    Stride_dequeue PID: 1, stride: 4294967294
    Stride_enqueue PID: 1, stride: 4294967294
    Stride_pick PID: 1, stide: 2147483645
    Stride_dequeue PID: 1, stride: 2147483645
    all user-mode processes have quit.
    init check memory pass.
    kernel panic at kern/process/proc.c:460:
        initproc exit.

    Welcome to the kernel debug monitor!!
    Type 'help' for a list of commands.
    K> qemu: terminating on signal 2
