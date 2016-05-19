## 问题1：FIFO

#### a) 访问6

命令：

	./disksim.py   -a 6 -c
	
结果：

	Block:   6  Seek:  0  Rotate:345  Transfer: 30  Total: 375

	TOTALS      Seek:  0  Rotate:345  Transfer: 30  Total: 375
	
#### b) 访问30

命令：

	./disksim.py   -a 30 -c
	
结果：

	Block:  30  Seek: 80  Rotate:265  Transfer: 30  Total: 375
	
	TOTALS      Seek: 80  Rotate:265  Transfer: 30  Total: 375

	
#### c) 访问7,30,8

命令：

	./disksim.py   -a 7,30,8 -c
	
结果：
	
#### d) 访问10,11,12,13，24,1

命令：

	./disksim.py   -a 6
	
结果：

	Block:   7  Seek:  0  Rotate: 15  Transfer: 30  Total:  45
	Block:  30  Seek: 80  Rotate:220  Transfer: 30  Total: 330
	Block:   8  Seek: 80  Rotate:310  Transfer: 30  Total: 420

	TOTALS      Seek:160  Rotate:545  Transfer: 90  Total: 795
	
#### e) 访问10,11,12,13,24,1

命令：

	./disksim.py   -a 10,11,12,13,24,1 -c
	
结果：

	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  12  Seek: 40  Rotate:320  Transfer: 30  Total: 390
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  24  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	Block:   1  Seek: 80  Rotate:280  Transfer: 30  Total: 390

	TOTALS      Seek:160  Rotate:965  Transfer:180  Total:1305
	
## 问题2：	SSTF

命令：
	
	./disksim.py   -a 10,11,12,13,24,1 -c -p SSTF
	
结果

	Block:  10  Seek:  0  Rotate:105  Transfer: 30  Total: 135
	Block:  11  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:   1  Seek:  0  Rotate: 30  Transfer: 30  Total:  60
	Block:  12  Seek: 40  Rotate:260  Transfer: 30  Total: 330
	Block:  13  Seek:  0  Rotate:  0  Transfer: 30  Total:  30
	Block:  24  Seek: 40  Rotate:260  Transfer: 30  Total: 330

	TOTALS      Seek: 80  Rotate:655  Transfer:180  Total: 915
	