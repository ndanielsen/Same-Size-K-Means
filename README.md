## Equal Groups K-Means Clustering

This is a k-means variation that produces clusters of the same size utilizing the
scikit-learn Kmeans methods and associated utilities.

The same-size k-Means logic is the same as found in the Elki Same-size k-Means Variation tutorial.

https://elki-project.github.io/tutorial/same-size_k_means

Please note that this implementation only works in scikit-learn 17.X as later
versions having breaking changes to this implementation. Also sparse matrices
are not yet supported.

## Usage

Use just like you would utilize the [scikit-learn Kmeans](http://scikit-learn.org/0.17/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans) class

> from clustering.equal_groups import EqualGroupsKMeans
>
> import numpy as np
>
> X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
>
> clf = EqualGroupsKMeans(n_clusters=2)
>
> clf.fit(X)
>
> clf.labels_
>




## Performance

The performance of this implementation is very slow. It is relatively quick if
the number observations is less than 500.

Optimizations are readily accepted via pull-requests.

## To Dos
- More test coverage
- Add support for sparse matrices
- Package for pypi
- Potentially speed up with cython
- scikit-learn 18.X implementation
