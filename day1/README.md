Here is my solutions for day1,

Here I'll write the runtimes and an idea of how it works.
For part 1, simply finding the two numbers that add up to 2020 and multiply these two togather, by sorting the list it becomes something that can be done in linear
time. Thus for part 1 it is upperbounded by the time it takes to sort a list which will be O(nlgn).
For part 2, we can utilze the knowledge from part 1, but here we need to find 3 numbers that add up to 2020. Thus, we will need to include an overarching loop that will take
n time to go through, and then for each element we can do a linear search for elements that add up to 2020 by going from the ends. Thus the run time for the overall part is O(n^2)
