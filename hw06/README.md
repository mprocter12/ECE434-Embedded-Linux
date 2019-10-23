Mark Procter
ECE434
Homework 6


Video Questions:

1) Julia Cartwright is a Software Engineer at National Instruments
2) PREEMPT_RT is known as "the rt patch" is a patchset ontop of the vanilla Linux kernel which helps provide bound timing guarantees for user task execution, a required property for any real-time application.
3) Mixed criticality is when a system handles two levels of criticality, safety and non-safety, and run them at the same time
4) Drivers can misbehave due to issues with the scheduler, shared kernel or the satck between rt and non-rt
5) The delta is the schedule latency
6) Cyclictest is when you take a timestamp, sleep for a set duration, then take another time stamp and get the difference between the actual time slept and the set duration to get latency
7) Figure 2 is the plotted form of the results from the cyclictest
8) Dispatch latency is the difference between hardware firing and the thread scheduler being told the thread to run. Scheduler latency is the difference between the scheduler knowing what to run and the thread actually being ran. 
9) Mainline is a single process that is running and can contain multiple threads that are being switched on and off the process
10) Because of the architectual constraints, the CPU cannot disptach the interrupt until the read has finished
11) Because preempt_disable was called, the interrupts are silenced until preempt_enable is called


PREEMT_RT

The file that was generated from my tests is entitled UnderLoad.png, for a load I used the make and make clean from linux/modules folder from Dr. Yoder's exercises. 

The graph entitled NoLoad.png shows the difference between the no-rt and the PREEMPT_RT without any load put on the system.

## Prof. Yoder's comments
I expected the under load plots to look more different.

Late: -1
Grade:  9/10

Project wiki is missing.
