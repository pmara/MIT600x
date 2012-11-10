DERIVATIVES : 15.0 POINTS
=========================

For Newton's method, we will also need a way to find the derivative of a polynomial; that is, we will need to find `f'(x)`, where `f'(x)` is the derivative of `f(x)`.

Recall that the derivative of a polynomial f(x)=ax^b is `f'(x) = abx^(b-1)`, unless `b = 0`, in which case `f'(x) = 0`.

To compute the derivative of a polynomial function with many terms, you just do the same thing to every term individually. For example, if `f(x) = x^4 + 3x^3 + 17.5x^2 - 13.39`, then `f'(x) = 4x^3 + 9x^2 + 35x`.

Implement the computeDeriv function. This function computes the derivative of a polynomial function. It takes in a list of numbers poly and returns the derivative, which is also a polynomial represented by a list of floats.

Example Usage:

    # - 13.39 + 17.5x^2 + 3x^3 + x^4
    >>> poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
    >>> print computeDeriv(poly)
    [0.0, 35.0, 9.0, 4.0] # 35x + 9x^2 + 4x^3

You should implement this function on your own machine, in the file ps3_newton.py. Test your code well in Idle, and when you are convinced it is correct, cut and paste your definition into this tutor window.

Sample Test Cases
-----------------

Here are some example Test Cases to test your code with - feel free to make up your own additional test cases. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

	>>> print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
	[0.0, 35.0, 9.0, 4.0]
	>>> print computeDeriv([6, 1, 3, 0])
	[1.0, 6.0, 0.0]
	>>> print computeDeriv([20])
	[0.0]

Note that the polynomial your function returns must be a list of floats, not ints!
