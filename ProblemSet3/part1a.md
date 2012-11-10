POLYNOMIALS : 10.0 POINTS
=========================

For this problem set, we will be representing polynomials as lists. Remember that a polynomial is a sum of powers of a variable, each scaled by a coefficient, for example:

    p(x) = a0 + a1x + a2x^2 + ... + anx^n

We will use the index of a number in the list to represent the power, and the value at that index to represent the coefficient for that term. So for example, the polynomial `-13.39 + 17.5x^2 + 3x^3 + x^4` would be represented by the list `[-13.39, 0.0, 17.5, 3.0, 1.0]`. This is because the list represents `-13.39x^0 + 0.0x^1 + 17.5x^2 + 3.0x^3 + 1.0x^4`, which is the same as `-13.39 + 17.5x^2 + 3x^3 + x^4`.

Implement the evaluatePoly function. This function evaluates a polynomial function for a given value of x. So for example if

    f(x) = 5x^2 + 9.3x^3 + 7x^4

then

    f(-13) = 5(-13)2 + 9.3(-13)3 + 7(-13)4 = 180339.9

evaluatePoly takes in a list of numbers, poly and a number, x, where x can be a float or an int. evaluatePoly takes the polynomial represented by poly and computes its value at x. It returns this value as a float.

Example Usage:

    # f(x) = 5x^2 + 9.3x^3 + 7x^4
    >>> poly = [0.0, 0.0, 5.0, 9.3, 7.0]
    >>> x = -13
    >>> print evaluatePoly(poly, x)
    180339.9 # f(-13) = 5*(-13)^2 + 9.3*(-13)^3 + 7*(-13)^4

You should implement this function on your own machine, in the file ps3_newton.py. Test your code well in Idle, and when you are convinced it is correct, cut and paste your definition into this tutor window.

Sample Test Cases
-----------------

Here are some example Test Cases to test your code with - feel free to make up your own additional test cases. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

	>>> print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
	180339.9
	>>> print evaluatePoly([2, 0, 7, 1], 4)
	178.0
	>>> print evaluatePoly([-12], 3.7)
	-12.0
