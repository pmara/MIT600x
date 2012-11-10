NEWTON'S METHOD : 25.0 POINTS
=============================

Newton's method (also known as the Newton-Raphson method) is a successive approximation method for finding the roots of a function. Recall that the roots of a function f(x) are the values of x such that f(x)=0. You can read more about Newton's method here.

In this problem, we define an iteration as a specific computation to update our guess for the root. Thus, if your procedure gets lucky and finds a close enough answer using x0, that would be iteration 0.

Here is how Newton's method works:

 1. On the 0th iteration, we guess some x0.

 2. We check to see if it's a root or close enough to a root by calculating f(x0). If f(x0) is within some small value epsilon of 0, we say that's good enough and call x0 a root.

 3. If f(x0) is not good enough, we need to come up with a better guess, x1. The value of x1 is calculated by the equation:

        x1 = x0 - f(x0)/f'(x0)

 4. We check to see if x1 is close enough to a root. If it is not, we make an even better guess x2 and check that. And so on and so on.

    For every `xn` that is not close enough to a root, we replace it with `x(n+1) = xn - f(xn)/f'(xn)` and check if that is close enough to a root. We repeat until we finally find a value close to a root.

For simplicity, we will only be using polynomial functions in this problem set.

Implement the computeRoot function. This function applies Newton's method of successive approximation as described above to find a root of the polynomial function. It takes in a list of numbers poly, an initial guess x_0 that serves as the "0th iteration" of the method, and an error bound epsilon. It returns a list. The first element of this list is the root of the polynomial represented by poly, and the second element is the number of iterations it took to get to that root.

The function starts at x_0. It then applies Newton's method. It ends when it finds a root x such that the absolute value of f(x) is less than epsilon, i.e. when f(x) is close enough to zero. It returns the root it finds as a float. The root found does not have to equal the example provided to the exact decimal point.

Example Usage:

    # - 13.39 + 17.5x^2 + 3x^3 + x^4
    >>> poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print computeRoot(poly, x_0, epsilon)
    [0.80679075379635201, 7]

You should implement this function on your own machine, in the file ps3_newton.py. Test your code well in Idle, and when you are convinced it is correct, cut and paste your definition into this tutor window.

Sample Test Cases
-----------------

Here are some example Test Cases to test your code with - feel free to make up your own additional test cases. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

	>>> print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
	[0.806790753796352, 7]
	>>> print computeRoot([1, 9, 8], -3, .01)
	[-1.0000079170005467, 5]
	>>> print computeRoot([1, -1, 1, -1], 2, .001)
	[1.0002210630197605, 4]

Note that your answers should be close to this example output, but they don't have to match exactly. We'll expect the root you find to be within 0.001 of the example answer.

Note: You may use the functions evaluatePoly and computeDeriv directly, you do not have to copy your definitions into this box. We have provided definitions of these two functions that your code may call and use.
