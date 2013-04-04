INTRODUCTION
============

In problem set 6, you will build a program to monitor news feeds over the Internet. Your program will filter the news, alerting the user when it notices a news story that matches that user's interests (for example, the user may be interested in a notification whenever a story related to the Red Sox is posted).

This problem set has a lot of words, but don't get intimidated! The staff solution has about 80 lines of code; we recommend that the solutions you write for each problem should stay under about 15-20 lines of code (the solutions for some problems will be much shorter than that). If you find yourself writing way more code than that, you should ask for help on the discussion forum and look into alternative ways of implementing things in a simpler way.

We recommend starting early because there is a lot of reading here, but you ought to be able to do this problem set sequentially in the order that we've laid out. There are a lot of references on Python classes available (look for classes in the readings listed in the Reference Links section of the webpage); here is the official Python tutorial on classes, sections 9.1-9.7 (excepting 9.5.1) will be useful for this pset.

OBJECTIVES
----------

The goal of this problem set is to help you become familiar and comfortable with the following topics:

 - Many facets of object oriented programming, specifically:

    - Implementing new classes and their attributes.

    - Understanding class methods.

    - Understanding inheritance.

    - Telling the difference between a class and an instance of that class - recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.

 - Utilizing libraries as black boxes.

GETTING STARTED
===============

Download and save
-----------------

ProblemSet6.zip: A zip file of all the files you need, including:

 - ps6.py, a skeleton of the solution

 - ps6_test.py, a test suite that will help you check your answers

 - triggers.txt, a sample trigger configuration file. You may modify this file to try other trigger configurations

 - feedparser.py, a module that will retrieve and parse feeds for you

 - project_util.py, a module that includes a function to convert simple HTML fragments to plain text

The two modules (feedparser.py and project_util.py) are necessary for this lab to work, but you will not need to modify them. Feel free to read through them if you'd like to understand what's going on.

RSS OVERVIEW
============

Many websites have content that is updated on an unpredictable schedule. News sites, such as Google News, are a good example of this. One tedious way to keep track of this changing content is to load the website up in your browser, and periodically hit the refresh button. Fortunately, this process can be streamlined and automated by connecting to the website's RSS feed, using an RSS feed reader instead of a web browser (e.g. Sage). An RSS reader will periodically collect and draw your attention to updated content.

RSS stands for "Really Simple Syndication". An RSS feed consists of (periodically changing) data stored in an XML-format file residing on a web-server. For this project the details are unimportant. You don't need to know what XML is, nor do you need to know how to access these files over the network.

We will use a special Python module to deal with these low-level details. The higher-level details of the structure of the Google News RSS feed as described on the next page should be enough for our purposes.
