PROBLEM 5: TYPEWRITER : 15.0 POINTS
===================================

Imagine a typewriter: whenever it's in the middle of a word, and reaches its desired line length, the internal bell rings. This signifies to the typist that after finishing the current word, a newline must be manually inserted. Check out this cool video to see what it looks like! We ask you to emulate this process such that a newline is inserted as required after each word that exceeds the desired line length. Note that if the typewriter's bell rings on a space, a newline should be inserted before the start of the next word.

This function has to be recursive! You may not use loops (for or while) to solve this problem.

Hints
-----

A Few Helpful Thoughts

 - Write helper functions as appropriate. If you wish to use insertNewlines as a wrapper function that makes an appropriate call to a recursive function, please name your recursive helper function insertNewlinesRec so it can be properly graded by our automatic grader.

 - lineLength is not the maximum number of characters in the line. It is the length after which the next word should be wrapped to the next line.

 - Make sure that if a space occurs on the index of the desired line length, the next word is wrapped to the next line.

Test Cases
----------

Test case 1:

    >>> print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)

    While I expect
    new intellectual
    adventures ahead,
    nothing will compare
    to the exhilaration
    of the world-changing
    accomplishments
    that we produced
    together.

Test case 2:

    >>> print insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20)

    Nuh-uh! We let users
    vote on comments and
    display them by number
    of votes. Everyone knows
    that makes it impossible
    for a few persistent
    voices to dominate the
    discussion.
