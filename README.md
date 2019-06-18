# MIT-OCW-6.006 (Fall 2011)

### Problem set 1. Peak finding

In the filealgorithms.py, there are four different algorithms whichhave been written to solve the peak-finding problem, only some of which are correct. Your goal isto figure out which of these algorithms are correct and which are efficient.

### Problem set 2. Digital circuit simulation.

A combinational circuit is made up of gates, which are devices that take Boolean (True/ 1 andFalse/0) input signals, and output a signal that is a function of the input signals. Gates take sometime to compute their functions, so a gate’s output at timeτreflects the gate’s inputs at time τ−δ, where δ is the gate’s delay. For the purposes of this simulator, a gate’s output transitions between0 and 1 instantly.  Gates’ output terminals are connected to other gates’ inputs terminals by wires that propagate the signal instantly without altering it.

The circuit simulator takes an input file that describes a circuit layout,  including gates’ delays, probes  (indicating  the  gates  that  we  want  to  monitor  the  output),  and  external  inputs.   It  then simulates the transitions at the output terminals of all the gates as time progresses. It also outputs transitions at the probed gates in the order of the timing of those transitions.This problem will walk you through the best known approach for fixing performance issues in a system.  You will profile the code, find the performance bottleneck, understand the reason behind it, and remove the bottleneck by optimizing the code.

  Solved with implementation of priority queue algorithm. Priority queue data structure takes O(0) time to find Min element.


### Problem set 3. Digital circuit layout.

A chip consists of logic gates,  whose input and output terminals are connected by wires (very thin conductive traces on the silicon substrate).  AMDtel’s high-yield manufacturing process only allows for horizontal or vertical wires.  Wires must not cross each other, so that the circuit will function according to its specification.  This constraint is checked by the software tool that you will optimize. The topologies required by complex circuits are accomplished by having dozens of layers of wires that do not touch each other, and the tool works on one layer at a time.

The method that has the performance bottleneck is called from the CrossVerifier class. Upon reading the class, it seems that the original author was planning to implement a sweep-line algorithm, but couldn’t figure out the details, and bailed and implemented an inefficient method at the last minute. Fortunately, most of the infrastructure for a fast sweep-line algorithm is still in place.Furthermore, you notice that the source code contains a trace of the working sweep-line algorithm, in the good trace.jsonp file. Sweep-line algorithms are popular in computational geometry.  Conceptually, such an algorithm sweeps a vertical line left to right over the plane containing the input data, and performs operations when the line “hits” point of interest in the input.  This is implemented by generating an array containing all the points of interest, and then sorting them according to their position along the horizontal axis (x coordinate).

  Solved with implementation of Binary search tree, AVL tree + range query.

### Problem set 4. Matching DNA Sequences
