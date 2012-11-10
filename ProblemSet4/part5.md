PLAYING A GAME : 10.0 POINTS
============================

A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the playGame function. You should remove the code that is currently uncommented in the playGame body. Read through the specification and make sure you understand what this function accomplishes. For the game, you should use the HAND_SIZE constant to determine the number of cards in a hand.

Testing: Try out this implementation as if you were playing the game. Try out different values for HAND_SIZE with your program, and be sure that you can play the wordgame with different hand sizes by modifying only the variable HAND_SIZE.

Sample Output
-------------

Here is how the game output should look...


    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: tot
    "tot" earned 9 points. Total: 9 points

    Current Hand: p z u t
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 9 points.

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: top
    "top" earned 15 points. Total: 15 points

    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: tu
    Invalid word, please try again.

    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 15 points.

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a q w f f i p
    Enter word, or a "." to indicate that you are finished: paw
    "paw" earned 24 points. Total: 24 points

    Current Hand: q f f i
    Enter word, or a "." to indicate that you are finished: qi
    "qi" earned 22 points. Total: 46 points

    Current Hand: f f
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 46 points.

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a r e t i i n
    Enter word, or a "." to indicate that you are finished: inertia
    "inertia" earned 99 points. Total: 99 points.

    Run out of letters. Total score: 99 points.

    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e


Hints about the output
----------------------

Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in playHand - be sure that your code is modular and uses function calls to the playHand helper function!

You should also make calls to the dealHand helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.
Here is the above output, with the output from playHand obscured:

    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    <call to playHand> 
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    <call to playHand>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    <call to playHand>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

Hopefully this hint makes the problem seem a bit more approachable.

Mutation
--------

Please note that our implementation of playHand DOES mutate the hand. Be sure you pass in a copy of the hand to this function when you call it.

If you're not sure what this means, please review the Python docs on dictionaries. Especially of interest is the 'copy' function.
