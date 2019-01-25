from clustering.equal_groups import EqualGroupsKMeans

import numpy as np

X = np.array([[1, 2], [4, 4], [1, 0], [3, 2], [4, 4], [4, 0]])

clf = EqualGroupsKMeans(n_clusters=2)

clf.fit(X)

print (clf.labels_)
