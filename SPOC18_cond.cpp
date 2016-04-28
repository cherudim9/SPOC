/*

thread work1: in charge of producing frames
thread work2: in charge of producing wheels
thread consumer: in charge of producing bikes, using two wheels and one frame

cur_frames: currently produced and not used frames
avail_frames: number of frames to produce until now (work1 will stop once this reduces to 0)
cur_wheels: currently produced and not used wheels
avail_wheels: number of wheels to produce until now (work2 will stop once this reduces to 0)

mtx1: mutex used in generating frames
mtx2: mutex used in generating wheels

*/

#include <cstdio>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cstring>
#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(){

  mutex mtx1, mtx2, mtx_write;
  condition_variable work1_cond, work2_cond;

  int cur_frames=0, cur_wheels=0;
  int avail_frames=10, avail_wheels=25;
  int prod=0;

  cout<<"work1\twork2\tconsumer\tframes\twheels\tbikes\n";
  
  thread consumer([&]() {
      while(1){
        unique_lock<mutex> lck1(mtx1);
        unique_lock<mutex> lck2(mtx2);
        if (cur_wheels+avail_wheels<2 || cur_frames+avail_frames<1)
          break;
        while(cur_wheels<2 || cur_frames<1){
          if (avail_frames>0)
            work1_cond.wait(lck1);
          if (avail_wheels>0)
            work2_cond.wait(lck2);
        }
        cur_wheels-=2;
        cur_frames-=1;
        prod++;
        cout<<"\t\tp+1\t\t"<<cur_frames<<"\t"<<cur_wheels<<"\t"<<prod<<endl;     
      }
    });

  thread work1([&]() {
      while(avail_frames>0){
        //work1_cond.wait(lck);
        unique_lock<mutex> lck(mtx1);
        unique_lock<mutex> lck_write(mtx_write);  
        avail_frames--;
        cur_frames++;  
        cout<<"f+1\t\t\t\t"<<cur_frames<<"\t"<<cur_wheels<<"\t"<<prod<<endl;
        work1_cond.notify_all();
      }
      //work1_cond.notify_all();
    });

  thread work2([&]() {
      while(avail_wheels>0){
        //work2_cond.wait(lck);
        unique_lock<mutex> lck(mtx2);
        unique_lock<mutex> lck_write(mtx_write);
        avail_wheels--;
        cur_wheels++;
        cout<<"\tw+1\t\t\t"<<cur_frames<<"\t"<<cur_wheels<<"\t"<<prod<<endl;
        work2_cond.notify_all();
      }
      //work2_cond.notify_all();
    });

  consumer.join();
  work1.join();
  work2.join();

  return 0;
}
