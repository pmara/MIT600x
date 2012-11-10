GETTING STARTED
===============

This problem set has two parts. Part A deals with encryption, a very important concept in computer science. Part B is a set of problems designed to help you practice writing recursive functions.

Download and save ProblemSet5.zip. This zip archive includes the following files:

 - ps5_encryption.py: Skeleton code you'll fill in for Part A of the problem set.

 - words.txt: A list of English words

 - ps5_pseudo.txt: Pseudocode for Problem 2. We urge you to not look at this file until you reach Problem 2 and read the instructions contained there.

 - story.txt: An encoded story

 - ps5_recursion.py: Skeleton code for Part B of the problem set.

Load ps5_encryption.py into a Python environment without making any modifications to it, in order to ensure that everything is set up correctly. The code that we have given you loads a list of words from a file. If everything is okay, after a small delay, you should see the following printed out:

    Loading word list from file...
    55909 words loaded.

If you see an IOError instead (e.g., No such file or directory), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (this will vary based on where you saved the file).

The file ps5_encryption.py has a few functions already implemented that you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand everything else:

    # -----------------------------------
    # Helper code
    # (you don't need to understand this helper code)
    . . .
    # (end of helper code)
    # -----------------------------------
