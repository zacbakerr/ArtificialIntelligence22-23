This lab is about training a neural network to implement a logic function.  The submitted script receives a single argument, the name of a file that defines the logic gate.  The format of this file is a sequence of lines akin to:
1 0 1 => 1
On the left there is a sequence of space separated numbers.  This defines the inputs (and how many inputs).  The number of inputs is the same in any given file.  There is always an "=>" string to the right of which are the expected outputs.  The number of expected outputs is always the same for all lines in a file.  For this lab, each input is 0 or 1 and each output is supposed to be 0 or 1.  All but the last problem have a single output.  For this lab there will always be either 1, 2, 3, or 4 input values for the logic gate.

The submitted script is to construct a neural network in the allotted time (30 seconds) per logic gate.  Its output is to be a line with the text "Layer counts" followed by the layer counts on that same line.  The recommended layer counts for this lab are (1+ # of inputs) 2 1 1.  The layer counts imply weight counts and the following lines should have weights, each line corresponding to weights between one layer and the next.  Using the layer counts above, the weight counts would be: 2(1+# of inputs), 2, 1.  The reason for the 1+ is that it corresponds to a DC offset of 1.  If the first number of submitted layer counts is one greater than the number of inputs to the specified logic gate, then the grader will supply a constant 1 as an additional input value to the first layer of nodes.

The transfer function of the nodes should be the logistic function: 1/(1+e^(-x))

The grader will read in the NN weights that the submitted code outputs and run each line of the specified logic gate through it to determine the sum of all the errors.  The score for each problem is 0% if the sum exceeds 0.5, 50% if the sum is .05, 100% if this sum is <= .01, and linear between these values.

If the submitted code times out, the most recently output NN will be used for evaluation.  Note that code should assemble the NN to be printed into a single string and then print that NN with a single print statement so that the submitted code does not get stopped in the process of printing a NN (since in that case, no NN for that problem would be found, resulting in a score of 0% for that problem).