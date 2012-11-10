YOU AND YOUR COMPUTER
=====================

THIS PART OF THE PROBLEM SET IS OPTIONAL

> Due to technical difficulties, we have not been able to post a grader
> for this problem in a timely manner. In the interest of fairness, we
> are thus making this problem optional. We encourage you to implement
> this problem - you'll learn a lot, and have a really fun program to
> show off to friends and family!

Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function. You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.

A Note On Runtime
-----------------

You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the compChooseWord function.

Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).

IMPORTANT: Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.
