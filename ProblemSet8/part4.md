PROBLEM 4: IMPLEMENTING A SIMULATION WITH DRUGS : 10.0 POINTS
=============================================================

In this problem, we consider the effects of both administering drugs to the patient and the ability of virus particle offsprings to inherit or mutate genetic traits that confer drug resistance. As the virus population reproduces, mutations will occur in the virus offspring, adding genetic diversity to the virus population. Some virus particles gain favorable mutations that confer resistance to drugs.

RESISTANTVIRUS CLASS
--------------------

In order to model this effect, we introduce a subclass of SimpleVirus called ResistantVirus. ResistantVirus maintains the state of a virus particle's drug resistances, and accounts for the inheritance of drug resistance traits to offspring. Implement the ResistantVirus class.

TREATEDPATIENT CLASS : 10.0 POINTS
----------------------------------

We also need a representation for a patient that accounts for the use of drug treatments and manages a collection of ResistantVirus instances. For this, we introduce the TreatedPatient class, which is a subclass of Patient. TreatedPatient must make use of the new methods in ResistantVirus and maintain the list of drugs that are administered to the patient.

Drugs are given to the patient using the TreatedPatient class's addPrescription() method. What happens when a drug is introduced? The drugs we consider **do not directly kill virus particles lacking resistance to the drug**, but prevent those virus particles from reproducing (much like actual drugs used to treat HIV). Virus particles with resistance to the drug continue to reproduce normally. Implement the TreatedPatient class.
