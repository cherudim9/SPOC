
在lab7-answer中分析

#### 1. cvp->count含义是什么？cvp->count是否可能<0, 是否可能>1？请举例或说明原因。

- cvp->count：等待该条件变量的线程数；
- cvp->count不可能<0：因为cond_wait函数中对cvp->count的操作都是先加后减，总是成对出现；
- 大于1：当且仅当存在多个线程在等待这个条件变量。

#### 2. cvp->owner->next_count含义是什么？cvp->owner->next_count是否可能<0, 是否可能>1？请举例或说明原因。

- owner：cvp所在的管程；
- owner->next_count：由于发出signal_cv而睡眠的线程的个数；
- 不会小于0：对next_cound的操作总是成对出现，要么先加后减，要么先减后加；
- 不会大于1：当线程A执行signal_cv唤醒进程B，A睡眠，next_count++；进程B结束后先唤醒A，next_count--。

#### 3. 现在的管程（条件变量）实现是否有bug?

应该没有。


#### 4. 目前的lab7-answer中管程的实现是Hansen管程类型还是Hoare管程类型？请在lab7-answer中实现另外一种类型的管程。

Hoare



