PART III: FILTERING : 10.0 POINTS
=================================

At this point, you can run ps6.py, and it will fetch and display Google and Yahoo news items for you in little pop-up windows. How many news items? All of them.

Right now, the code we've given you in ps6.py gets all of the feeds every minute, and displays the result. This is nice, but, remember, the goal here was to filter out only the the stories we wanted.

PROBLEM 10
----------

Write a function, filterStories(stories, triggerlist) that takes in a list of news stories and a list of triggers, and returns a list of only the stories which a trigger fires for.

After completing Problem 10, run the file ps6_test.py. All the tests should now pass.

Also after completing Problem 10, you can try running ps6.py, and various RSS news items should pop up, filtered by some hard-coded triggers defined for you in some code near the bottom. The code runs an infinite loop, checking the RSS feed for new stories every 60 seconds. Press "Exit" at the bottom of the popup window to exit out of the program.
