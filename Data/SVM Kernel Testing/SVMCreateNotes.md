## Support Vector Machine Kernel Tests

The purpose of this page is to define the practical differences between each kernel.
Based on the all six attempts (tests), it appears that linear is the clear choice.
Not only was one of the fastest (slower than RBF but much faster than poly), it had high performance.
This performance was the case even with overfitted data (10,000 points).

### Attempt 1

Kernel = RBF (default)
Gamma = Auto (default)
Testing on training image: 99% accuracy
Worst Test Result: 78% accuracy
(In the rectangle: 38% accuracy)

### Attempt 2

Kernel = RBF (default)
Gamma = Scale
Cache_size = 500
Testing on training image: 97% accuracy
Best test result: 92% accuracy
Worst test result: 74% accuracy

I'm going to only record results based on inside the rectangle.

### Attempt 3

Since attempt 2 had such a major improvement, I decided to rerun attempt 1 with the same cache size.
So far, each prediction has been exactly the same which is pretty interesting.
I think for the rest of my attempts, I'm going to use gamma='scale' since the improvement was so dramatic.
Also, auto is way slower.
I confirmed that cache_size doesn't affect prediction.
Also, it took 29,028 iterations to learn.

### Attempt 4

Kernel = Linear
Testing on training image: 96% accuracy
Best test result: 95% accuracy
Worst test result: 76% accuracy

Holy crap, it ran for 64,906,910 iterations.
Each iteration was fairly fast but dang.
That took around 15 minutes it feels like.
At first glance, it looks like it drew a really smooth picture.
However, we can see that it had a really difficult time with background elements.

### Attempt 5

Kernel = Poly
Testing on training image: 95% accuracy
Best test result: 95% accuracy
Worst test result: 75% accuracy

Wow, and I thought linear took a long time.
1,167,284,911 iterations.
I feel like that took roughly 2.5 to 3 hours.
Let's see if it was worth it.
Looking at the results, it appears it wasn't better than linear.
Due to long run time and mediocre performance, linear looks like the winner.

### Attempt 6

Kernel = Sigmoid
Testing on training image: 54% accuracy
Best test result: 49% accuracy
Worst test result: 16% accuracy

Wow, sigmoid was crazily fast.
8,116 iterations.
Oh, it drew the arm, just complete backwards.
I have a feeling it'd improve with more data or more iterations.