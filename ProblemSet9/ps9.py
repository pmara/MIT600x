# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delay = 300
    treatmenttime = 150
    totaltime = delay + treatmenttime

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    populations = []
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
                        for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)

        for timestep in range(delay):
            patient.update()

        patient.addPrescription('guttagonol')

        for timestep in range(delay, totaltime):
            patient.update()

        populations.append( patient.getTotalPop() )

    pylab.hist(populations, bins=10)
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    pylab.show()

#simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delay1 = 150
    delay2 = 0
    totaltime = delay1 + delay2

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    populations = []
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
                        for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)

        for timestep in range(delay1):
            patient.update()

        patient.addPrescription('guttagonol')

        for timestep in range(delay2):
            patient.update()

        patient.addPrescription('grimpex')

        for timestep in range(delay1):
            patient.update()

        populations.append( patient.getTotalPop() )

    pylab.hist(populations, bins=10)
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    pylab.show()

simulationTwoDrugsDelayedTreatment(100)
