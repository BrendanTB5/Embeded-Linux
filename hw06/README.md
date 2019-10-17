# HW 6

### What Every Driver Developer Should Know about RT

1. Where does Julia Cartwright work?
	- National Instruments
2. What is PREEMT_RT?
	- PREEMT_RT is a linux kernel patch that turns linux into a real time operating system.
3. What is mixed criticality?
	- Running mutliple tasks that need to run together, one that needs real time requirements, and stuff that doesn't need to happen in real time, like monitoring.
4. How can drivers misbehave?
	- Driver stacks are usually shared between RT and non RT reliant applications.
5. What is Δ in Figure 1?
	- Latency between an external event occuring, and a real time task running at. RT systems want to bound this.
6. What is Cyclictest?
	- Takes a time stamp, sleeps for a fixed duration, sleeps for a fixed duration, and then finds out when another timestamp is taken, showing how long it takes for the application to be run again.
7. What is plotted in Figure 2?
	- A comparison of unloaded cyclictest with the PREEMPT_RT kernel in green and the regular kernel in purple.
8. What is dispatch latency? Scheduling latency?
	- Dispatch latency is the ammount of time between the hardware firing and the scheduler being told to run the applicaiton.
	- Scheduling latency is the latency between the scheduler finding out that the application needs to run, and actually running the code on the CPU.
9.  What is mainline?
	- Mainline are how non RT systems handle interrpts.
10. What is keeping the External event in Figure 3 from starting?
	- The non-critical IRQ is running and will not check for an interurpt event until it has utilized its given scheduler tiime or given it back to the scheduler.
11. Why can the External event in Figure 4 start sooner?
	- The interupts force the scheduler to give the small program in the HardIRQ context for that small program to call the actual task in non hard irq space.

## PREEMPT_RT

I ran the given PREMPT_RT tests with the loaded situations utilizing the command:
`cat /dev/urandom | gzip -9 > /dev/null`
This is because I was unable to utilize gcc in the RT kernel.
### Loaded Test
[![Loaded Test](https://github.com/Thebester5/Embeded-Linux/blob/master/hw06/busy.png?raw=true "Loaded Test")](https://github.com/Thebester5/Embeded-Linux/blob/master/hw06/busy.png?raw=true "Loaded Test")
### Unloaded Test
[![](https://github.com/Thebester5/Embeded-Linux/blob/master/hw06/notbusy.png?raw=true)](https://github.com/Thebester5/Embeded-Linux/blob/master/hw06/notbusy.png?raw=true)

While the responses look similar between the two kernels for both cases, the divert as time goes on. The RT kernel in the loaded case has a bound of about 105us, compared to the non RT kernel which does not seem to have a bound.This case also holds true for the nonloaded case.
