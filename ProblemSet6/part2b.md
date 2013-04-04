PART II: TRIGGERS : 15.0 POINTS
===============================

COMPOSITE TRIGGERS
------------------

So the triggers from the previous page are mildly interesting, but we want to do better: we want to 'compose' the earlier triggers, to set up more powerful alert rules. For instance, we may want to raise an alert only when both "google" and "stock" were present in the news item (an idea we can't express right now).

Note that these triggers are not word triggers and should not be subclasses of WordTrigger.

PROBLEM 6
---------

Implement a NOT trigger (NotTrigger).

This trigger should produce its output by inverting the output of another trigger. The NOT trigger should take this other trigger as an argument to its constructor (why its constructor? Because we can't change what parameters evaluate takes in...that'd break our polymorphism). So, given a trigger T and a news item x, the output of the NOT trigger's evaluate method should be equivalent to not T.evaluate(x).

When this is done, the NotTrigger unit tests should pass.

PROBLEM 7
---------

Implement an AND trigger (AndTrigger).

This trigger should take two triggers as arguments to its constructor, and should fire on a news story only if both of the inputted triggers would fire on that item.

When this is done, the AndTrigger unit tests should pass.

PROBLEM 8
---------

Implement an OR trigger (OrTrigger).

This trigger should take two triggers as arguments to its constructor, and should fire if either one (or both) of its inputted triggers would fire on that item.

When this is done, the OrTrigger unit tests should pass.
