# MIT-OCW-6.006 (Fall 2011)

### Problem set 2. Digital circuit simulation.

Acombinational circuitis made up ofgates, which are devices that take Boolean (True/ 1 andFalse/0) input signals, and output a signal that is a function of the input signals. Gates take sometime to compute their functions, so a gate’s output at timeτreflects the gate’s inputs at timeτ−δ,whereδis the gate’s delay. For the purposes of this simulator, a gate’s output transitions between0 and 1 instantly.  Gates’ output terminals are connected to other gates’ inputs terminals bywiresthat propagate the signal instantly without altering it.

The circuit simulator takes an input file that describes a circuit layout,  including gates’ delays,probes  (indicating  the  gates  that  we  want  to  monitor  the  output),  and  external  inputs.   It  thensimulates the transitions at the output terminals of all the gates as time progresses. It also outputstransitions at the probed gates in the order of the timing of those transitions.This problem will walk you through the best known approach for fixing performance issues in asystem.  You will profile the code, find the performance bottleneck, understand the reason behindit, and remove the bottleneck by optimizing the code.

  Solved with implementation of priority queue algorithm. Priority queue data structure takes O(0) time to find Min element.


### Problem set 3. Digital circuit layout.



