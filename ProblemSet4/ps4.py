# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials, verbose=False):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    trials = [300, 150, 75, 0]
    results = {}
    for iters in trials:
        if verbose:
            print("Starting {} trial...".format(iters))
        junk1, junk2, final_count = simulationWithDrug(time_to_drug=iters,
                                                       numTrials=numTrials,
                                                       verbose=verbose)
        results[iters] = final_count
        del junk1, junk2

    # Here we find the smallest value
    smallest = min(list(x[0] for x in results.values()))
    largest = max(list(x[-1] for x in results.values()))
    rang = (smallest, largest)

    pylab.figure()
    pylab.title("{} Different Times for Delayed Drug Introduction".format(
                len(results)))
    pylab.subplot(221)
    pylab.hist(results[300], label='300', bins=20, range=rang)
    pylab.subplot(222)
    pylab.hist(results[150], label='150', bins=20, range=rang)
    pylab.subplot(223)
    pylab.hist(results[75], label='75', bins=20, range=rang)
    pylab.subplot(224)
    pylab.hist(results[0], label='0', bins=20, range=rang)
    pylab.show()


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials, verbs=False):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def simulationWithDrug(numViruses=100, maxPop=1000,
                           maxBirthProb=0.1, clearProb=0.05,
                           resistances={'guttagonol': False, 'grimpex':False},
                           mutProb=0.005, numTrials=numTrials,
                           time_drugone=150, time_drugtwo=150, close_steps=150,
                           verbose=False, show_flag=False):
        """
        Runs simulations and plots graphs for problem 5.

        For each of numTrials trials, instantiates a patient, runs a simulation for
        150 timesteps, adds guttagonol, and runs the simulation for an additional
        150 timesteps.  At the end plots the average virus population size
        (for both the total virus population and the guttagonol-resistant virus
        population) as a function of time.

        numViruses: number of ResistantVirus to create for patient (an integer)
        maxPop: maximum virus population for patient (an integer)
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: maximum clearance probability (a float between 0-1)
        resistances: a dictionary of drugs that each ResistantVirus is resistant to
                    (e.g., {'guttagonol': False})
        mutProb: mutation probability for each ResistantVirus particle
                (a float between 0-1).
        numTrials: number of simulation runs to execute (an integer)

        """

        def DrawFigure():    # Draw the graph!
            pylab.figure()
            pylab.title("Average Virus Population over {} Time Steps".format(
                        time_steps))
            pylab.subplot(211)
            pylab.ylabel("Virus Population")
            pylab.xlabel("Time Steps")
            # pylab.ylim(0, 1100)
            # pylab.xkcd()
            pylab.plot(averaged_total, 'r', label='Total')
            pylab.plot(grim_resistant_viruses, 'b-', label='Grimpex Resistant')
            pylab.plot(gutt_resistant_viruses, 'g.',
                       label='Guttagonol Resistant')
            pylab.legend(loc='best')
            pylab.subplot(212)
            pylab.hist(final_virus_count, bins=20)
            pylab.show()

        # Debugging!
        # Initialize the data-storing variables
        time_steps = time_drugone + time_drugtwo + close_steps
        total_viruses = []
        gutt_resistant_viruses = []
        grim_resistant_viruses = []
        averaged_total = []
        averaged_grim_resistant = []
        averaged_gut_resistant = []
        final_virus_count = []
        for index in range(time_steps):
            total_viruses.append(0)
            grim_resistant_viruses.append(0)
            gutt_resistant_viruses.append(0)
            # averaged_steps.append(0)

        # Here we do the main looping!
        for i in range(numTrials):
            # Debugging!
            if verbose:
                print("Beginning trial number {:>4} of {}".format(i, numTrials))
            # Initialize the trial variables
            virus_list = []
            for index in range(numViruses):
                virus_list.append(ResistantVirus(maxBirthProb, clearProb,
                                                resistances, mutProb))
            patient = TreatedPatient(virus_list, maxPop)
            for i in range(time_steps):
                if i == time_drugone:
                    patient.addPrescription('guttagonol')
                if i == time_drugtwo:
                    patient.addPrescription('grimpex')
                total_viruses[i] += patient.update()
                if verbose > 1:
                    print("Trial {} Adding resistant viruses: {} Total: {}".format(
                        i, patient.getResistPop(['guttagonol']),
                        resistant_viruses[i]))
                gutt_resistant_viruses[i] += patient.getResistPop(['guttagonol'])
                grim_resistant_viruses[i] += patient.getResistPop(['grimpex'])
                if i == time_steps - 1:
                    final_virus_count.append(patient.getTotalPop())
        # Average the data:
        for index in range(time_steps):
            averaged_total.append(total_viruses[index] / float(numTrials))
            averaged_grim_resistant.append(grim_resistant_viruses[index] / float(numTrials))
            averaged_gut_resistant.append(gutt_resistant_viruses[index] / float(numTrials))
        # Debugging!
        if verbose > 1:
            print("Here's the averages: \n{}".format(averaged_total))
            print("\nHere's the resistant averages: \n{}".format(
                averaged_resistant))
            print("\nHere are the final virus totals: \n{}".format(
                final_virus_count))
        final_virus_count.sort()
        if show_flag is True:
            DrawFigure()
        else:
            return averaged_total, final_virus_count

    trials = [300, 150, 75, 0]
    results = {}
    for iters in trials:
        if verbs:
            print("Starting {} iteration".format(iters))
        junk1, final_count = simulationWithDrug(time_drugtwo=iters,
                                                       numTrials=numTrials,
                                                       verbose=verbs)
        results[iters] = final_count
        del junk1

    # Here we find the smallest value
    smallest = min(list(x[0] for x in results.values()))
    largest = max(list(x[-1] for x in results.values()))
    rang = (smallest, largest)

    pylab.figure()
    pylab.title("{} Different Times for Delayed Drug Introduction".format(
                len(results)))
    pylab.subplot(221)
    pylab.hist(results[300], label='300', bins=20, range=rang)
    pylab.subplot(222)
    pylab.hist(results[150], label='150', bins=20, range=rang)
    pylab.subplot(223)
    pylab.hist(results[75], label='75', bins=20, range=rang)
    pylab.subplot(224)
    pylab.hist(results[0], label='0', bins=20, range=rang)
    pylab.show()
