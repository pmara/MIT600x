PART II: TRIGGERS : 5.0 POINTS
==============================

PHRASE TRIGGERS
---------------

At this point, you have no way of writing a trigger that matches on "New York City" -- the only triggers you know how to write would be a trigger that would fire on "New" AND "York" AND "City" -- which also fires on the phrase "New students at York University love the city". It's time to fix this. Since here you're asking for an exact match, we will require that the cases match, but we'll be a little more flexible on word matching. So, "New York City" will match:

 - New York City sees movie premiere
 - In the heart of New York City's famous cafe
 - New York Cityrandomtexttoproveapointhere

but will not match:

 - I love new york city
 - I love    New                 York                  City!!!!!!!!!!!!!!

PROBLEM 9
---------

Implement a phrase trigger (PhraseTrigger) that fires when a given phrase is in any of the story's subject, title, or summary. The phrase should be an argument to the class's constructor. You may find the Python operator in helpful, as in:

    >>> print "New York City" in "In the heart of New York City's famous cafe"
    True
    >>> print "New York City" in "I love new york city"
    False

When this is done, the PhraseTrigger unit tests should pass.
