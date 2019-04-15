## Support Vector Machine Kernel Tests

The purpose of this page is to define the practical differences between each kernel.


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
Testing on training image:
Best test result:
Worst test result:

### Attempt 6

Kernel = Sigmoid
Testing on training image:
Best test result:
Worst test result: