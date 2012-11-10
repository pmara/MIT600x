COMPUTER PLAYS A HAND
=====================

THIS PART OF THE PROBLEM SET IS OPTIONAL

> Due to technical difficulties, we have not been able to post a grader
> for this problem in a timely manner. In the interest of fairness, we
> are thus making this problem optional. We encourage you to implement
> this problem - you'll learn a lot, and have a really fun program to
> show off to friends and family!

Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to Part A's playHand function (get the hint?).

Implement the compPlayHand function. This function should allow the computer to play a given hand, using the procedure you just wrote in the previous part. This should be very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand will be different.

Be sure to test your function on some randomly generated hands using dealHand.

Test Cases
----------

Some test cases to look at:

compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)

    Current Hand:
    a p p s e l
    "appels" earned 110 points. Total: 110 points
    Total score: 1100 points.

compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)

    Current Hand:
    a a c b t
    "acta" earned 24 points. Total: 24 points
    Current Hand:
    b
    Total score: 24 points.

compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)

    Current Hand:
    a a e e i i m m n n t t
    "immanent" earned 96 points. Total: 96 points
    Current Hand:
    a e t i
    "ait" earned 9 points. Total: 105 points
    Current Hand:
    e
    Total score: 105 points.
