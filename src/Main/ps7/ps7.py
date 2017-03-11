# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Collaborators:
# Time:

import numpy
from numpy import random
import pylab


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


class SimpleVirus(object):
    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        #Floats between 0-1

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

    def doesClear(self):
        z = random.rand(1).__getitem__(0)
        if z > self.clearProb:
            return False
        else:
            return True

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

    def reproduce(self, popDensity):
        f = random.random()
        if self.maxBirthProb * (1 - popDensity) > f:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            return False


        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """


class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        self.virn = viruses
        self.viruses = []
        for j in range(self.virn):
                self.viruses.append(SimpleVirus(0.1, 0.05))
        self.maxPop = maxPop

        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

    def getTotalPop(self):
        return int(self.viruses.__len__())

        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """

    def update(self):
        """make list of survivors and then from those make list of children using probability, simple stuff"""
        survivors = []
        for a in range(self.viruses.__len__()):
            if not self.viruses.__getitem__(a).doesClear():
                survivors.append(self.viruses.__getitem__(a))

        self.viruses = survivors
        density = self.viruses.__len__() / self.maxPop

        for b in range(self.viruses.__len__()):
            if self.viruses.__getitem__(b).reproduce(density) and self.viruses.__len__() < self.maxPop:
                self.viruses.append(SimpleVirus(self.viruses.__getitem__(b).maxBirthProb,
                                                self.viruses.__getitem__(b).clearProb))

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        - The current population density is calculated. This population density
          value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """


def simulationWithoutDrug():
    x_axis = []
    y_axis = []
    pat = SimplePatient(100, 1000)
    for i in range(100):
        pat.update()
        x_axis.append(i)
        y_axis.append(pat.viruses.__len__())
    pylab.plot(x_axis, y_axis)
    pylab.xlabel("time")
    pylab.legend("pop")
    pylab.ylabel("virus population")
    pylab.title("Viral growth simulation "
                + "\n" + "Steps: " + str(i+1)
                + "\n" + "Final population " + str(pat.viruses.__len__()))
    pylab.show()
simulationWithoutDrug()


