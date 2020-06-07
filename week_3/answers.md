# Week 3 answers

## Exercise 1

The problem is solved by evaluating the equation that equals the PDF of s1 with a loss L, and the PDF of s2 with a loss 2L.

N(mu=7, std=1) / N(mu=5, std=0.5) = 2

Finding the point in x-axis in which this relationship is true solves the problem, giving a trivial solution and the sought one.

## Exercise 2

The prior is 1e-8 for having the disease, so it very unlikely in the population. We shall assume that having the disease is the equivalent to a stimulus. The tests are thought as the response to the stimulus when they are positive. By the Bayes' rule,

p(s|r) * p (r) = p(r|s) * p(s) 

From the data,
p(s) = 1e-8
p(r) is unknown
p(r|s) = 0.99
p(r|not s) = 0.02


Given the accuracy rates provided, we know that it is far more LIKELY that when a patient is tested positive, it is because that patient is positive. This is so because in the maximum-likelihood approach we pay attention to the term p(r|s). Therefore, the answer is **YES**.

## Exercise 3

Now, following a Maximum A Posteriori approach, as the very same name suggests, we must look at the information we get after we make the observation(s). The quantity of interest is now p(s|r), this is, the probability of having the disease after a positive response. 
Since we follow an a posteriori approach, it immediately follows that 

p(s|r) = p(r|s) * p(s) / p(r) = 0.99 * 1e-8 / 1 

which is almost zero. Thus, the answer is **NO**.

## Exercise 4

The driver of such difference in the answers is the role the prior plays on each.
In the first case, the prior provides relatively little information to the question, for even though it is very unlikely to have the disease, once you have it, it is extremely likely that your test yields a positive result (99% of the time). 
However in the MAP estimation, the prior is telling us that the probability that any patient suffers from the disease is extremely low.
