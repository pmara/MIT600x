PROBLEM 1: THE EFFECT OF DELAYING TREATMENT ON PATIENT DISEASE : 30.0 POINTS
========================================================================

In this problem, we explore the effect of delaying treatment on the ability of the drug to eradicate the virus population. You will need to run multiple simulations to observe trends in the distributions of patient outcomes.

In problem 5 of the last pset you ran a simulation that consists of 150 time steps, followed by the addition of the drug, guttagonol, followed by another 150 time steps. Run the same simulation as in problem 5 in pset 8 but this time for 300, 150, 75, and 0 time steps before administering guttagonol to the patient. Then, run the simulation for an additional 150 time steps. Use the same initialization parameters for ResistantVirus and TreatedPatient as you did for problem 5 of pset 8.

Use the following parameters to initialize a TreatedPatient:

 - viruses, a list of 100 ResistantVirus instances

 - maxPop, maximum sustainable virus population = 1000

Each ResistantVirus instance in the viruses list should be initialized with the following parameters:

 - maxBirthProb, maximum reproduction probability for a virus particle = 0.1

 - clearProb, maximum clearance probability for a virus particle = 0.05

 - resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}

 - mutProb, probability of a mutation in a virus particle's offspring = 0.005

For each of these 4 conditions, repeat the experiment for enough trials to gain reasonable insight into the expected result. Rather than averaging the final virus population across different trials as in the last pset, this time use pylab's hist() function to plot a histogram of the final virus populations under each condition for each trial. You may also find pylab's subplot function to be helpful. The x-axis of the histogram should be the final total virus population values (choose x axis increments or "histogram bins" according to the range of final virus population values you get by running the simulation multiple times). Then, the y-axis of the histogram should be the number of trials belonging to each histogram bin. You should decide the number of trials you ran for each condition in order to obtain a reasonable distribution. Briefly justify your decision in your writeup.

Fill in the function simulationDelayedTreatment(numTrials) to perform this simulation. Feel free to break down the problem into smaller subparts and define helper functions for each.

> Hint: It may take some time to run enough trials to arrive at a
> distribution for each condition. Debug your code using a small number
> of trials. Once your code is debugged, use a larger number of trials
> and expect the simulation to take a few minutes. The simulation should
> take about 3-6 minutes to run a reasonable number of trials. You may
> also find it helpful to divide the tasks and write helper functions to
> do each subpart, and then have the simulationDelayedTreatment function
> call the helper functions and keep track of the final results.
