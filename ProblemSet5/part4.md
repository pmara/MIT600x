PROBLEM 4: ERICIAN : 15.0 POINTS
================================

A word is considered erician if it contains the letters e, r, i, and c in it, in that order. For example, we would say that the following words are erician: "meritocracy", "generic", "derrick", "euphoric", "heretic", and "electric", because they each contain those four letters in the correct order. The word "rice" is not erician because the four letters appear in the wrong order.

In this problem, we want you to write a more generalized function called x_ian(x, word) that returns True if all the letters of x are contained in word in the same order as they appear in x. For example:

    >>> x_ian('eric', 'algebraic')
    True
    >>> x_ian('john', 'mahjong')
    False
    >>> x_ian('alvin', 'palavering')
    True
    >>> x_ian('sarina', 'czarina')
    False

This function has to be recursive! You may not use loops (for or while) to solve this problem.
