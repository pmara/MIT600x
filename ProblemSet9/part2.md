PROBLEM 2: DESIGNING A TREATMENT PLAN WITH TWO DRUGS : 30.0 POINTS
==================================================================

One approach to addressing the problem of acquired drug resistance is to use cocktails – administration of multiple drugs that act independently to attack the virus population.

In this problem, we use two independently-acting drugs to treat the virus. We will use this model to decide the best way of administering the two drugs. Specifically, we examine the effect of a lag time between administering the first and second drugs on patient outcomes.

Use the following parameters to initialize a TreatedPatient:

 - viruses, a list of 100 ResistantVirus instances.

 - maxPop, maximum sustainable virus population = 1000

Each ResistantVirus instance in the viruses list should be initialized with the following parameters:

 - maxBirthProb, maximum reproduction probability for a virus particle = 0.1

 - clearProb, maximum clearance probability for a virus particle = 0.05

 -resistances, the virus’s genetic resistance to drugs in the experiment: {'guttagonol': False, 'grimpex': False}

 - mutProb, probability of a mutation in a virus particle’s offspring = 0.005

Run the simulation for 150 time steps before administering guttagonol to the patient. Then run the simulation for 300, 150, 75, and 0 time steps before administering a second drug, grimpex, to the patient. Finally, run the simulation for an additional 150 time steps.

For each of these 4 conditions, repeat the experiment for enough trials to get a reasonable condition, while recording the final virus populations. Use pylab’s hist() function to plot a histogram of the final total virus populations under each condition.

> HINT: As with Problem 1, the simulation will take a few minutes to
> run. Use print statements to monitor the simulation’s progress.

Fill in the function `simulationTwoDrugsDelayedTreatment(numTrials)` to perform this simulation. Feel free to break down the problem into smaller subparts and define helper functions for each.

Create 4 histograms (for 300, 150, 75, and 0 time steps) and then answer the following set of questions.

 1. If you consider final virus particle counts of 0-50 to be cured (or in remission), approximately what percentage of patients were cured (or in remission) at the end of the simulation?
    1. delay of 2nd drug = 300
    2. delay of 2nd drug = 150
    3. delay of 2nd drug = 75
    4. delay of 2nd drug = 0

 2. What is the relationship between when drugs are applied and patients being cured?

 3. Increasing mutProb will increase the number of cured patients.

 4. The relationship between number of cured patients and when the delay occurs linear.

 5. Of the four delay values tested, which has the lowest variance?
