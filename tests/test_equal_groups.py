from clustering.equal_groups import EqualGroupsKMeans

import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])


def test_evens():
    assert 1 + 1 == 2

def test_evens_imports():
    clf = EqualGroupsKMeans(n_clusters=2, random_state=0)
    clf.fit(X)
    clf.labels_
    clf.cluster_centers_
    predict = clf.predict([[0, 0], [4, 4]])
    print(clf.inertia_)
    assert clf.inertia_ != 0
